#!/usr/bin/env python
import wx

def OnFrameExit(event):
    quit()

class NoteWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu= wx.Menu()

        filemenu.Append(wx.ID_NEW, "New"," Start a new Note")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_SAVE, "Save"," Save your note")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_SAVEAS, "Save as"," Save your note to a specific directory")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit"," Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)
        self.Show(True)

        #Adds a button event listener to exit the program.
        self.Bind(wx.EVT_MENU, OnFrameExit, id=wx.ID_EXIT)

app = wx.App(False)
frame = NoteWindow(None, "Sample editor")
frame.Center()
app.MainLoop()