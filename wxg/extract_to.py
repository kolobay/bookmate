#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.0 on Sun Jun  7 21:21:33 2015
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class ExtractTo(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ExtractTo.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Panel.__init__(self, *args, **kwds)
        self.label_extract_notes = wx.StaticText(self, wx.ID_ANY, _("The place to put the extraced files:"))
        self.radio_btn_extract_remove = wx.RadioButton(self, wx.ID_ANY, _("The same directory as the archive file"))
        self.radio_btn_extract_exto = wx.RadioButton(self, wx.ID_ANY, _("Extract To:"))
        self.text_ctrl_extract_path = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_extract_path = wx.Button(self, wx.ID_ANY, _("..."))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ExtractTo.__set_properties
        self.SetSize((758, 535))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ExtractTo.__do_layout
        sizer_extract_to = wx.BoxSizer(wx.VERTICAL)
        sizer_extract_exto = wx.BoxSizer(wx.HORIZONTAL)
        sizer_extract_to.Add(self.label_extract_notes, 0, wx.EXPAND, 0)
        sizer_extract_to.Add(self.radio_btn_extract_remove, 0, wx.TOP, 5)
        sizer_extract_exto.Add(self.radio_btn_extract_exto, 0, wx.TOP, 5)
        sizer_extract_exto.Add(self.text_ctrl_extract_path, 1, wx.ALIGN_BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        sizer_extract_exto.Add(self.button_extract_path, 0, 0, 0)
        sizer_extract_to.Add(sizer_extract_exto, 0, wx.EXPAND, 2)
        self.SetSizer(sizer_extract_to)
        self.Layout()
        # end wxGlade

# end of class ExtractTo
class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        config = ExtractTo(None, wx.ID_ANY, "")
        self.SetTopWindow(config)
        config.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    gettext.install("BookMateConfig") # replace with the appropriate catalog name

    BookMateConfig = MyApp(0)
    BookMateConfig.MainLoop()