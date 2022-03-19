
from .board_clean import board_cleaner
from .Clean_board_GUI import clean_boardGUI
import os
import wx

class clean_dialog(clean_boardGUI):
    def __init__(self,parent):
        #this class inherets dialog
        super(clean_boardGUI, self).__init__(parent)

        mop = board_cleaner()
    def on_ok(self,event):

        #get checkboxes
        hide_des        = self.chkbox_hide_des.GetValue()
        hide_des_fab    = self.chkbox_hide_des_fab.GetValue()
        unhide_des      = self.chkbox_exclude_des.GetValue()
        hide_val        = self.chkbox_hide_val.GetValue()
        unhide_val      = self.chkbox_exclude_val.GetValue()

        #get lists and split
        des_list = self.Des_hide_list.GetValue()
        des_list = des_list.split(',')

        val_list = self.val_hide_list.GetValue()
        val_list = val_list.split(',')

        #clean
        self.mop.hide(hide_des, hide_val, des_list, val_list, hide_des_fab, unhide_des, unhide_val )


    def on_cancel(self, event):
        event.Skip()
        self.Destroy()

class clean_dialog_plugin(pcbnew.ActionPlugin):
    def __init__(self):
        super(clean_dialog_plugin, self).__init__()

        self.frame = None

        self.name = "Board Cleaner"
        self.category = "Cleaning"
        self.description = "Remove common part designatiors from silkscreen, such as resistors and caps"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')
    
    def defaults(self):
        pass

    def Run(self):
        self.frame = wx.FindWindowByName("PcbFrame")

        dlg = clean_dialog(self.frame)
        dlg.CenterOnParent()



