#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.0 on Fri May 15 23:19:24 2015
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class SameName(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SameName.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Panel.__init__(self, *args, **kwds)
        self.label_smn_from = wx.StaticText(self, wx.ID_ANY, _("Compare Directory:"))
        self.text_ctrl_smn_from_path = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_smn_from_path = wx.Button(self, wx.ID_ANY, _("..."))
        self.label_smn_to = wx.StaticText(self, wx.ID_ANY, _("With Directory:"))
        self.text_ctrl_smn_to_path = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_smn_to_path = wx.Button(self, wx.ID_ANY, _("..."))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SameName.__set_properties
        self.SetSize((871, 546))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SameName.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(2, 3, 0, 0)
        grid_sizer_1.Add(self.label_smn_from, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.text_ctrl_smn_from_path, 1, wx.ALIGN_BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_1.Add(self.button_smn_from_path, 0, 0, 0)
        grid_sizer_1.Add(self.label_smn_to, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.text_ctrl_smn_to_path, 1, wx.ALIGN_BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_1.Add(self.button_smn_to_path, 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableCol(1)
        self.Layout()
        # end wxGlade

    def setSameName(self, comp_dir, with_dir):
        if comp_dir:
            self.text_ctrl_smn_from_path.SetValue(comp_dir)
        if with_dir:
            self.text_ctrl_smn_to_path.SetValue(with_dir)


# end of class SameName
class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        same_name = SameName(None, wx.ID_ANY, "")
        self.SetTopWindow(same_name)
        same_name.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    gettext.install("BookMateConfig") # replace with the appropriate catalog name

    BookMateConfig = MyApp(0)
    BookMateConfig.MainLoop()
