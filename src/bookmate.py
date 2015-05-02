#!/usr/bin/python
# -*- coding: utf-8 -*-

"BookMate: Your friendly book management tool implemented by WxPython"

import wx
#import os, sys
#import glob, shutil, thread
from pySearch import pySearch
from pyConfig import pyConfig
from pySketch import pySketch
from bookDatabase import BookDatabase


Name	= 'BookMate'
Version	= '0.0.1-dev'
Author	= 'Deng Chunhui'
Email	= 'chunchengfh@gmail.com'
Date	= '2015.04.13'
ABOUT   = "Your friendly book management tool implemented by WxPython"

WIN_WIDTH = 1000
WIN_HEIGH = 640

CFG_FILE = "bookmate.cfg"
#LIST_COLORS = [wx.GREEN, wx.BLUE, wx.RED]
LIST_COLORS = [wx.GREEN, 'gray', '#00aabb']


class MyFrame(wx.Frame):
	"Main frame for BookMate"

	def __init__(self, parent=None, id=-1, title='BookMate',
			pos=wx.DefaultPosition, size=wx.DefaultSize):
		wx.Frame.__init__(self, None, -1, title, pos, size)
		self.panel = wx.Panel(self)
		#self.panel.SetBackgroundColour('white')
		self.nb = wx.Notebook(self.panel)

		self.createMenuBar()
		self.createStatusBar()
		self.createToolBar()

		self.config_frame = pyConfig(self.nb)
		self.main_panel_frame = pySearch(self.nb)
		self.remove_dupli_frame = pySketch(self.nb)
		self.batch_rename_frame = pySketch(self.nb)
		self.batch_extract_frame = pySketch(self.nb)

		self.nb.AddPage(self.config_frame, "Configuration")
		self.nb.AddPage(self.main_panel_frame, "Quick Search")
		self.nb.AddPage(self.remove_dupli_frame, "Remove Duplications")
		self.nb.AddPage(self.batch_rename_frame, "Batch Rename")
		self.nb.AddPage(self.batch_extract_frame, "Batch Extract")

		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(self.nb, 1, wx.EXPAND)
		self.panel.SetSizer(box)
		#box.Fit(self)

		self.init_config()


	def restore_config(self, file):  # TODO
		return ['.']

	def init_config(self):
		self.datapaths = self.restore_config(CFG_FILE)
		self.bookdb = BookDatabase(self.datapaths)
		self.main_panel_frame.orig_booklist = self.bookdb.to_booklist()
		self.main_panel_frame.list_ctrl_1.set_value(self.main_panel_frame.orig_booklist)

	def menu_data(self):
		return [ ("&File", (
				("&Save Result", "Save Search Result", self.mypass),
				("", "", ""),
				("C&onfigure...", "Configure Search Options", self.mypass),
				("", "", ""),
				("&Close", "Close this tool", self.onExit))),
			 ("&Action", (
				("&Find", "Find", self.mypass),
				("&Open", "Open", self.mypass),
				("&Open Dir", "Open Dir", self.mypass),
				("&Copy To", "Copy Selected Files to Another Place", self.mypass),
				("&Delete", "Delete Selected Files", self.mypass),
				("", "", ""),
				("&Clear Result\tCTRL-Q", "Clear Search Result", self.onClearResult))),
			 ("&Help", (
				("&Help Contents\tF1", "Help of this tool", self.onHelp),
				("&About", "About this tool", self.onAbout))) ]


	def createMenuBar(self):
		menuBar = wx.MenuBar()
		for eachMenuData in self.menu_data():
			menuLabel = eachMenuData[0]
			menuItems = eachMenuData[1]
			menuBar.Append(self.createMenu(menuItems), menuLabel)
		self.SetMenuBar(menuBar)


	def createMenu(self, menuitems):
		menu = wx.Menu()
		for each_menu in menuitems:
			if each_menu[0] == '':
				menu.AppendSeparator()
			else:
				tmpmenu = menu.Append(wx.NewId(), each_menu[0], each_menu[1])
				self.Bind(wx.EVT_MENU, each_menu[2], tmpmenu)

		return menu


	def mypass(self, event):
		pass

	def createToolBar(self):
		toolbar = self.CreateToolBar()
		tb_config = toolbar.AddSimpleTool(-1, wx.Bitmap('images/configure.png'),
				"Configuration",
				"Configure BookMate")
		tb_samefile = toolbar.AddSimpleTool(-1, wx.Bitmap('images/find.png'),
				"Find Same File",
				"Find all the same files with or without the same name")
		toolbar.Realize()

		self.Bind(wx.EVT_MENU, self.onConfig, tb_config)
		self.Bind(wx.EVT_MENU, self.onSameFile, tb_samefile)


	def createStatusBar(self):
		self.CreateStatusBar()
		self.SetStatusText('Welcome to use BookMate!')


	def onSameFile(self, event):
		dupli_files = self.bookdb.get_duplicate_booklist()
		self.main_panel_frame.list_ctrl_1.DeleteAllItems()
		for num, booklist in enumerate(dupli_files):
			color = LIST_COLORS[num % len(LIST_COLORS)]
			self.main_panel_frame.list_ctrl_1.set_value(booklist, color)


	def onConfig(self, event):
		wx.MessageBox('No Configuration yet', 'Configuration', wx.OK | wx.ICON_INFORMATION, self)


	def onClearResult(self, event):
		self.main_panel_frame.onClearResult(event)


	def onHelp(self, event):
		wx.MessageBox('Sorry, No help yet', 'Help', wx.OK | wx.ICON_INFORMATION, self)

	def onAbout(self, event):
		#about = (Name 	+ '\nThis is another PyFind implemented by WxPython'
		about = (Name 	+ '\n' + ABOUT
				+ '\n\nVersion: ' + Version
				+ '\n Author: ' + Author
				+ '\n Email: ' + Email
				+ '\n Date:\t' + Date)
		wx.MessageBox(about, 'About %s' %Name, wx.OK | wx.ICON_INFORMATION, self)

	def onExit(self, event):
		#save_config()
		self.Close()



class BookMate(wx.App):
	"Main App for BookMate"

	def OnInit(self):
		#restore_config()
		self.frame = MyFrame(self, size=(WIN_WIDTH, WIN_HEIGH))
		self.frame.Center()
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

#	thread.start_new(myprint, ())

if __name__ == '__main__':
	bookMate = BookMate(False)
	bookMate.MainLoop()
