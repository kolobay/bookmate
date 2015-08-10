#!/usr/bin/python
#
# Copyright (C) 2015, Chunis Deng (<chunchengfh@gmail.com>)
#
# This file is part of BookMate and is released under the terms of
# GNU GPLv3 License, see doc/LICENSE for details.
#

import sys, os
import time
import wx
from pyCommon import CommonListCtrl, find_str

#LIST_COLORS = [wx.GREEN, wx.BLUE, wx.RED]
#LIST_COLORS = [wx.GREEN, 'gray', '#00aabb']
LIST_COLORS = ['#ffffcc', '#cccccc', '#cccc99']

# how to process duplicated files
[PROCESS_DELETE, PROCESS_NO_PROCESS, PROCESS_MOVE] = range(1, 4)


class DupListCtrl(CommonListCtrl):
	def __init__(self, parent, id):
		CommonListCtrl.__init__(self, parent, id)

	def set_value(self, booklist, color):
		for book in booklist:
			mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(book.mtime))
			#size = str(book.size/1024) + 'K'

			item = (book.name, str(book.size), mtime, book.abspath)
			index = self.InsertStringItem(sys.maxint, item[0])
			for col, text in enumerate(item[1:]):
				self.SetStringItem(index, col+1, text)
			self.SetItemData(index, index)
			self.itemDataMap[index] = item
			self.SetItemBackgroundColour(index, color)
			self.SetItemTextColour(index, book.color)


class PyDuplication(wx.Panel):
	def __init__(self, *args, **kwds):
                self.orig_booklist = []  # this is a list of same_files_list
		self.asked_booklist = []  # this is the list of search result
		self.co_dupli_keep = 2
		self.co_dupli_destiny = PROCESS_DELETE
		self.co_abs_dupsomewhere = ""

		self.mark_green_id = wx.NewId()
		self.mark_red_id = wx.NewId()
		self.open_file_id = wx.NewId()
		self.open_dir_id = wx.NewId()
		self.clear_id = wx.NewId()
		self.copy_id = wx.NewId()
		self.move_id = wx.NewId()
		self.amazon_id = wx.NewId()
		self.douban_id = wx.NewId()

		# begin wxGlade: PySearch.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Panel.__init__(self, *args, **kwds)
		self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
		self.text_ctrl_1.SetFocus()
		# self.list_ctrl_1 = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
		self.list_ctrl_1 = DupListCtrl(self, -1)

		self.__do_layout()
		#self.files = open(DB_FILE).readlines()
		#self.files = [ x.strip() for x in self.files ]
		#self.ufiles = [ x.decode('utf-8') for x in self.files ]
		#self.list_ctrl_1.set_value(self.ufiles)
		self.valstr = []

		self.Bind(wx.EVT_TEXT, self.doSearch, self.text_ctrl_1)

		self.list_ctrl_1.Bind(wx.EVT_CONTEXT_MENU, self.onRightClick)
		self.list_ctrl_1.Bind(wx.EVT_CHAR, self.onEsc)
		self.text_ctrl_1.Bind(wx.EVT_CHAR, self.onEsc)

		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: PySearch.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.VERTICAL)
		sizer_2.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)
		sizer_2.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
		sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		self.Layout()
		# end wxGlade


	def onEsc(self, event):
		key_code = event.GetKeyCode()
		# print "Key: ", key_code
		if key_code == 27:	# ESC pressed
			search_str = self.text_ctrl_1.GetValue()
			if search_str != "":
				self.text_ctrl_1.SetValue("")
			else:
				self.Close()
		else:
			event.Skip()

	def markColor(self, color):
		fullname = self.list_ctrl_1.getFullName()
		# print "fullname: %s" %fullname
		for books in self.orig_booklist:
			for book in books:
				if os.path.join(book.abspath, book.name) == fullname:
					book.color = color
		self.list_ctrl_1.markColor(color)

	def onMarkGreen(self, event):
		self.markColor(wx.GREEN)

	def onMarkRed(self, event):
		self.markColor(wx.RED)

	def onRightClick(self, event):
		#print 'Right click now...'
		menu = wx.Menu()

		menu.Append(self.mark_green_id, "Mark as Green")
		menu.Append(self.mark_red_id, "Mark as Red")
		menu.AppendSeparator()
		menu.Append(self.open_file_id, "Open")
		menu.Append(self.open_dir_id, "Open Directory")
		menu.Append(self.copy_id, "Copy to...")
		menu.Append(self.move_id, "Move to...")
		menu.AppendSeparator()
		menu.Append(self.amazon_id, "Search in Amazon.com")
		menu.Append(self.douban_id, "Search in Douban.com")

		self.Bind(wx.EVT_MENU, self.onMarkGreen, id = self.mark_green_id)
		self.Bind(wx.EVT_MENU, self.onMarkRed, id = self.mark_red_id)
		self.Bind(wx.EVT_MENU, self.list_ctrl_1.onOpenItem, id = self.open_file_id)
		self.Bind(wx.EVT_MENU, self.list_ctrl_1.onOpenDir, id = self.open_dir_id)
		self.Bind(wx.EVT_MENU, self.list_ctrl_1.onCopy, id = self.copy_id)
		self.Bind(wx.EVT_MENU, self.list_ctrl_1.onMove, id = self.move_id)
		self.Bind(wx.EVT_MENU, self.list_ctrl_1.onAmazon, id = self.amazon_id)
		self.Bind(wx.EVT_MENU, self.list_ctrl_1.onDouban, id = self.douban_id)

		self.PopupMenu(menu)
		menu.Destroy()


	def showBooklist(self, mybooklist):
		for num, booklist in enumerate(mybooklist):
			color = LIST_COLORS[num % len(LIST_COLORS)]
			self.list_ctrl_1.set_value(booklist, color)

	def onFindSameFile(self):
		dupli_files = self.bookdb.get_duplicate_booklist(self.co_dupli_keep - 1)
		self.bookdb.mark_color(dupli_files)
		self.orig_booklist = dupli_files

		self.list_ctrl_1.DeleteAllItems()
		self.showBooklist(self.orig_booklist)

	def onProcessSameFile(self):
		print "On pyDuplication: onProcessSameFile (TODO)"
		if self.co_dupli_destiny == PROCESS_NO_PROCESS:
			wx.MessageBox('Per config, nothing will be done for files marked in RED',
					'Process Duplication', wx.OK | wx.ICON_INFORMATION, self)
		elif self.co_dupli_destiny == PROCESS_DELETE:
			removed_books = []
			for bklist in self.asked_booklist:
				for book in bklist:
					if book.color == wx.RED:
						bklist.remove(book)
						removed_books.append(book)
						book.delete_myself()
			for book in removed_books:
				for bklist in self.orig_booklist:
					if book in bklist:
						bklist.remove(book)
			self.list_ctrl_1.DeleteAllItems()
			self.showBooklist(self.asked_booklist)
		elif self.co_dupli_destiny == PROCESS_MOVE:  # TODO
			print "Move to %s" %slef.co_abs_dupsomewhere


	def doSearch(self, event): # wxGlade: PySearch.<event_handler>
		self.list_ctrl_1.DeleteAllItems()

		search_str = self.text_ctrl_1.GetValue()
		#print search_str

		self.asked_booklist = []
		for mylist in self.orig_booklist:
			self.asked_booklist.append(find_str(mylist, search_str))
		self.showBooklist(self.asked_booklist)
		# event.Skip()

# end of class PySearch


class testFrame(wx.Frame):
	def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition, size=wx.DefaultSize):
		wx.Frame.__init__(self, parent, -1, pos=pos, size=size)
		self.panel = PyDuplication(self)

class MyApp(wx.App):
	def OnInit(self):
		self.frame = testFrame(pos=(300,120), size=(320, 200))
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True


if __name__ == '__main__':
	myapp = MyApp()
	myapp.MainLoop()
