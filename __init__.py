# -*- coding: utf-8 -*-
try:
    # Note the relative import!
    from .action_board_clean import clean_dialog
    # Instantiate and register to Pcbnew
    clean_dialog().register()
    # if failed, log the error and let the user know
except Exception as e:

    import wx
    wx.MessageBox('cleaner', f"Something went wrong: \n {e}", wx.OK | wx.ICON_ERROR)
