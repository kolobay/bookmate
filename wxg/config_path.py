#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.7.0 on Fri May 15 23:16:36 2015
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class ConfigPath(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ConfigPath.__init__
        wx.Panel.__init__(self, *args, **kwds)
        self.bookmate_config_panel = wx.Panel(self, wx.ID_ANY)
        self.label_search_path1 = wx.StaticText(self.bookmate_config_panel, wx.ID_ANY, _("  Search Directory 1:"), style=wx.ALIGN_RIGHT)
        self.combo_box_search_path1 = wx.ComboBox(self.bookmate_config_panel, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.button_path1 = wx.Button(self.bookmate_config_panel, wx.ID_ANY, _("Browse..."))
        self.label_search_path2 = wx.StaticText(self.bookmate_config_panel, wx.ID_ANY, _("Search Directory 2:"), style=wx.ALIGN_RIGHT)
        self.combo_box_search_path2 = wx.ComboBox(self.bookmate_config_panel, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.button_path2 = wx.Button(self.bookmate_config_panel, wx.ID_ANY, _("Browse..."))
        self.label_search_path3 = wx.StaticText(self.bookmate_config_panel, wx.ID_ANY, _("Search Directory 3:"), style=wx.ALIGN_RIGHT)
        self.combo_box_search_path3 = wx.ComboBox(self.bookmate_config_panel, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.button_path3 = wx.Button(self.bookmate_config_panel, wx.ID_ANY, _("Browse..."))
        self.label_search_path4 = wx.StaticText(self.bookmate_config_panel, wx.ID_ANY, _("Search Directory 4:"), style=wx.ALIGN_RIGHT)
        self.combo_box_search_path4 = wx.ComboBox(self.bookmate_config_panel, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.button_path4 = wx.Button(self.bookmate_config_panel, wx.ID_ANY, _("Browse..."))
        self.label_expath1 = wx.StaticText(self.bookmate_config_panel, wx.ID_ANY, _("Exclude Directory 1:"), style=wx.ALIGN_RIGHT)
        self.combo_box_expath1 = wx.ComboBox(self.bookmate_config_panel, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.button_expath1 = wx.Button(self.bookmate_config_panel, wx.ID_ANY, _("Browse..."))
        self.label_expath2 = wx.StaticText(self.bookmate_config_panel, wx.ID_ANY, _("Exclude Directory 2:"), style=wx.ALIGN_RIGHT)
        self.combo_box_expath2 = wx.ComboBox(self.bookmate_config_panel, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.button_expath2 = wx.Button(self.bookmate_config_panel, wx.ID_ANY, _("Browse..."))

        self.__set_properties()
        self.__do_layout()

        # end wxGlade

        self.Bind(wx.EVT_BUTTON, self.onBrowsePath1, self.button_path1)

    def __set_properties(self):
        # begin wxGlade: ConfigPath.__set_properties
        self.SetSize((758, 535))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ConfigPath.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_exclude_path = wx.FlexGridSizer(2, 3, 0, 0)
        grid_sizer_search_path = wx.FlexGridSizer(4, 3, 0, 0)
        grid_sizer_search_path.Add(self.label_search_path1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_search_path.Add(self.combo_box_search_path1, 0, wx.EXPAND, 0)
        grid_sizer_search_path.Add(self.button_path1, 0, wx.LEFT | wx.RIGHT, 5)
        grid_sizer_search_path.Add(self.label_search_path2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_search_path.Add(self.combo_box_search_path2, 0, wx.EXPAND, 0)
        grid_sizer_search_path.Add(self.button_path2, 0, wx.LEFT | wx.RIGHT, 5)
        grid_sizer_search_path.Add(self.label_search_path3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_search_path.Add(self.combo_box_search_path3, 0, wx.EXPAND, 0)
        grid_sizer_search_path.Add(self.button_path3, 0, wx.LEFT | wx.RIGHT, 5)
        grid_sizer_search_path.Add(self.label_search_path4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_search_path.Add(self.combo_box_search_path4, 0, wx.EXPAND, 0)
        grid_sizer_search_path.Add(self.button_path4, 0, wx.LEFT | wx.RIGHT, 5)
        grid_sizer_search_path.AddGrowableCol(1)
        sizer_1.Add(grid_sizer_search_path, 0, wx.EXPAND, 0)
        grid_sizer_exclude_path.Add(self.label_expath1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_exclude_path.Add(self.combo_box_expath1, 0, wx.EXPAND, 0)
        grid_sizer_exclude_path.Add(self.button_expath1, 0, wx.LEFT | wx.RIGHT, 5)
        grid_sizer_exclude_path.Add(self.label_expath2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_exclude_path.Add(self.combo_box_expath2, 0, wx.EXPAND, 0)
        grid_sizer_exclude_path.Add(self.button_expath2, 0, wx.LEFT | wx.RIGHT, 5)
        grid_sizer_exclude_path.AddGrowableCol(1)
        sizer_1.Add(grid_sizer_exclude_path, 0, wx.EXPAND | wx.TOP, 10)
        self.bookmate_config_panel.SetSizer(sizer_1)
        sizer_3.Add(self.bookmate_config_panel, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        self.Layout()
        # end wxGlade

    def onBrowsePath1(self, event):
        dir = wx.DirDialog(None, "Choose a Directory:")
        if dir.ShowModal() == wx.ID_OK:
                self.path1 = dir.GetPath()
                self.combo_box_search_path1.SetValue(self.path1)
        dir.Destroy()

    def setPath(self, dirs):
        def mySetValue(obj, value):
            if value:
                obj.SetValue(value)

        mySetValue(self.combo_box_search_path1, dirs[0])
        mySetValue(self.combo_box_search_path2, dirs[1])
        mySetValue(self.combo_box_search_path3, dirs[2])
        mySetValue(self.combo_box_search_path4, dirs[3])
        mySetValue(self.combo_box_expath1, dirs[4])
        mySetValue(self.combo_box_expath2, dirs[5])

    def getPath(self):
        dir1 = self.combo_box_search_path1.GetValue()
        dir2 = self.combo_box_search_path2.GetValue()
        dir3 = self.combo_box_search_path3.GetValue()
        dir4 = self.combo_box_search_path4.GetValue()
        exdir1 = self.combo_box_expath1.GetValue()
        exdir2 = self.combo_box_expath2.GetValue()
        return (dir1, dir2, dir3, dir4, exdir1, exdir2)


# end of class ConfigPath
class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        config = ConfigPath(None, wx.ID_ANY, "")
        self.SetTopWindow(config)
        config.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    gettext.install("BookMateConfig") # replace with the appropriate catalog name

    BookMateConfig = MyApp(0)
    BookMateConfig.MainLoop()
