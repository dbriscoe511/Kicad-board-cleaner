
from .board_clean import board_cleaner
from .Clean_board_GUI import clean_boardGUI
import os
import wx
import pcbnew
import logging
import sys

class clean_dialog(clean_boardGUI):
    def SetSizeHints(self, sz1, sz2):
        # DO NOTHING
        pass

    def __init__(self,parent,mop,logger):
        #this class inherets dialog
        super(clean_dialog, self).__init__(parent)
        
        self.mop = mop
        self.logger = logger
        logger.info("clean dialog init successful")

        

    def on_apply(self, event):

        self.logger.info("Changes Applied")

        #get checkboxes
        hide_des        = self.chkbox_hide_des.GetValue()
        unhide_des      = self.chkbox_exclude_des.GetValue()
        hide_val        = self.chkbox_hide_val.GetValue()
        unhide_val      = self.chkbox_exclude_val.GetValue()
        change_des_text = self.chkbox_ch_des.GetValue()
        change_val_text = self.chkbox_ch_val.GetValue()

        #get lists and split
        des_list = self.Des_hide_list.GetValue()
        des_list = des_list.split(',')

        val_list = self.val_hide_list.GetValue()
        val_list = val_list.split(',')

        #get text properties into a dict
        text_properties = { "x_des_size" :      self.x_des_size.GetValue(),
                            "y_des_size" :      self.y_des_size.GetValue(),
                            "width_des_size" :  self.width_des_size.GetValue(),
                            "x_val_size" :      self.x_val_size.GetValue(),
                            "y_val_size" :      self.y_val_size.GetValue(),
                            "width_val_size" :  self.width_val_size.GetValue() }

        #clean
        self.mop.hide(hide_des, hide_val, des_list, val_list, unhide_des, unhide_val, change_des_text, change_val_text, text_properties)
          
    
    def on_ok(self,event):

        self.logger.info("Changes oked")
        self.on_apply(event)
        

        event.Skip()
        self.Destroy()


    def on_cancel(self, event):
        self.logger.info("User canceled the dialog")
        logging.shutdown()

        event.Skip()
        self.Destroy()

class clean_dialog_plugin(pcbnew.ActionPlugin):
    def __init__(self):
        super(clean_dialog_plugin, self).__init__()

        self.frame = None

        self.name = "Board Cleaner"
        self.category = "Cleaning"
        self.description = "Remove common part designatiors from silkscreen, such as resistors and caps"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'iconx24.png')
        self.dark_icon_file_name = os.path.join(os.path.dirname(__file__), 'iconx24.png')
    
        self.debug_level = logging.INFO

        self.plugin_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.version_file_path = os.path.join(self.plugin_folder, 'version.txt')

        # load the plugin version
        with open(self.version_file_path) as fp:
            self.version = fp.readline()


    def defaults(self):
        pass

    def Run(self):
        self.frame = wx.FindWindowByName("PcbFrame")
        board = pcbnew.GetBoard()
        pass

        # go to the project folder - so that log will be in proper place
        os.chdir(os.path.dirname(os.path.abspath(board.GetFileName())))

        # Remove all handlers associated with the root logger object.
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        file_handler = logging.FileHandler(filename='board-cleaner.log', mode='w')
        handlers = [file_handler]
        # set up logger
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)s %(lineno)d:%(message)s',
                            datefmt='%m-%d %H:%M:%S',
                            handlers=handlers)
        logger = logging.getLogger(__name__)
        logger.info("Plugin executed on: " + repr(sys.platform))
        logger.info("Plugin executed with python version: " + repr(sys.version))
        logger.info("KiCad build version: " + str(pcbnew.GetBuildVersion()))
        logger.info("Plugin version: " + self.version)
        logger.info("Frame repr: " + repr(self.frame))

        logger.info("Showing dialog")
        mop = board_cleaner(board,logger)

        dlg = clean_dialog(self.frame,mop,logger)
        dlg.CenterOnParent()

        # find position of right toolbar
        toolbar_pos = self.frame.FindWindowById(pcbnew.ID_V_TOOLBAR).GetScreenPosition()
        #logger.info("Toolbar position: " + repr(toolbar_pos))

        # find site of dialog
        size = dlg.GetSize()
        # place the dialog by the right toolbar
        dialog_position = wx.Point(toolbar_pos[0] - size[0], toolbar_pos[1])
        #logger.info("Dialog position: " + repr(dialog_position))
        dlg.SetPosition(dialog_position)

        dlg.Show()



