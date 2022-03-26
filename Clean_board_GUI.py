# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class clean_boardGUI
###########################################################################

class clean_boardGUI ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Clean board", pos = wx.DefaultPosition, size = wx.Size( 380,575 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.Size( 313,575 ), wx.DefaultSize )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Designators list ( or * for all)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText52.Wrap( -1 )

        bSizer14.Add( self.m_staticText52, 0, wx.ALL, 5 )

        self.Des_hide_list = wx.TextCtrl( self, wx.ID_ANY, u"R,C,L,D,H", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.Des_hide_list, 0, wx.ALL, 5 )

        self.chkbox_hide_des = wx.CheckBox( self, wx.ID_ANY, u"Hide listed designators from silkscreen", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_hide_des.SetValue(True)
        self.chkbox_hide_des.SetToolTip( u"Replicate only footprints that are in the same group as anchor (selected) footprint" )

        bSizer14.Add( self.chkbox_hide_des, 0, wx.ALL, 5 )

        self.chkbox_exclude_des = wx.CheckBox( self, wx.ID_ANY, u"Unhide designators excluded from list", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_exclude_des.SetToolTip( u"Replicate also locked footprints" )

        bSizer14.Add( self.chkbox_exclude_des, 0, wx.ALL, 5 )

        self.chkbox_ch_des = wx.CheckBox( self, wx.ID_ANY, u"Change listed designator text properties on silkscreen", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_ch_des.SetToolTip( u"Replicate only footprints that are in the same group as anchor (selected) footprint" )

        bSizer14.Add( self.chkbox_ch_des, 0, wx.ALL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText521 = wx.StaticText( self, wx.ID_ANY, u"x size (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText521.Wrap( -1 )

        bSizer5.Add( self.m_staticText521, 0, wx.ALL, 5 )


        bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText5211 = wx.StaticText( self, wx.ID_ANY, u"y size (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5211.Wrap( -1 )

        bSizer5.Add( self.m_staticText5211, 0, wx.ALL, 5 )


        bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText5212 = wx.StaticText( self, wx.ID_ANY, u"width (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5212.Wrap( -1 )

        bSizer5.Add( self.m_staticText5212, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer5, 1, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.x_des_size = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.x_des_size, 0, wx.ALL, 5 )


        bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.y_des_size = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.y_des_size, 0, wx.ALL, 5 )


        bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.width_des_size = wx.TextCtrl( self, wx.ID_ANY, u"0.15", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.width_des_size, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer3, 1, wx.EXPAND, 5 )


        bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Values list ( or * for all)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText51.Wrap( -1 )

        bSizer14.Add( self.m_staticText51, 0, wx.ALL, 5 )

        self.val_hide_list = wx.TextCtrl( self, wx.ID_ANY, u"R,C,L", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.val_hide_list, 0, wx.ALL, 5 )

        self.chkbox_hide_val = wx.CheckBox( self, wx.ID_ANY, u"Hide listed values", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_hide_val.SetValue(True)
        bSizer14.Add( self.chkbox_hide_val, 0, wx.ALL, 5 )

        self.chkbox_exclude_val = wx.CheckBox( self, wx.ID_ANY, u"Unhide values excluded from list", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.chkbox_exclude_val, 0, wx.ALL, 5 )

        self.chkbox_ch_val = wx.CheckBox( self, wx.ID_ANY, u"Change listed value text properites", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.chkbox_ch_val, 0, wx.ALL, 5 )

        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5213 = wx.StaticText( self, wx.ID_ANY, u"x size (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5213.Wrap( -1 )

        bSizer51.Add( self.m_staticText5213, 0, wx.ALL, 5 )


        bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText52111 = wx.StaticText( self, wx.ID_ANY, u"y size (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText52111.Wrap( -1 )

        bSizer51.Add( self.m_staticText52111, 0, wx.ALL, 5 )


        bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText52121 = wx.StaticText( self, wx.ID_ANY, u"width (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText52121.Wrap( -1 )

        bSizer51.Add( self.m_staticText52121, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer51, 1, wx.EXPAND, 5 )

        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

        self.x_val_size = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer31.Add( self.x_val_size, 0, wx.ALL, 5 )


        bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.y_val_size = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer31.Add( self.y_val_size, 0, wx.ALL, 5 )


        bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.width_val_size = wx.TextCtrl( self, wx.ID_ANY, u"0.15", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer31.Add( self.width_val_size, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer31, 1, wx.EXPAND, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.btn_cancel, 0, wx.ALL, 5 )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_apply = wx.Button( self, wx.ID_APPLY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.btn_apply, 0, wx.ALL, 5 )

        self.btn_ok = wx.Button( self, wx.ID_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.btn_ok, 0, wx.ALL, 5 )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer14.Add( bSizer15, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer14 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_cancel )
        self.chkbox_hide_val.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_exclude_val.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_ch_val.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.btn_cancel.Bind( wx.EVT_BUTTON, self.on_cancel )
        self.btn_apply.Bind( wx.EVT_BUTTON, self.on_apply )
        self.btn_ok.Bind( wx.EVT_BUTTON, self.on_ok )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_cancel( self, event ):
        event.Skip()

    def level_changed( self, event ):
        event.Skip()




    def on_apply( self, event ):
        event.Skip()

    def on_ok( self, event ):
        event.Skip()


