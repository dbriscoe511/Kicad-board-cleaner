# -*- coding: utf-8 -*-
try:
    # Note the relative import!
    from .action_board_clean import clean_dialog_plugin
    # Instantiate and register to Pcbnew
    clean_dialog_plugin().register()
    # if failed, log the error and let the user know
except Exception as e:

    import wx
    wx.MessageBox(f"Something went wrong: \n {e}", f"Something went wrong: \n {e}", wx.OK | wx.ICON_ERROR)
