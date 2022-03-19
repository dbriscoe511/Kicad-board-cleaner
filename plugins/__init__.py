
import board_clean
import Clean_board_GUI

class clean_dialog():
    def __init__(self,parent):
        #this class inherets dialog
        super(Clean_board_GUI, self).__init__(parent)

        mop = board_clean.board_cleaner()
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


