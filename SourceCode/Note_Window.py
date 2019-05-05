#!/usr/bin/env python
import wx
import sys
import MyPanel
import Note

ID_BUTTON1=300

def OnFrameExit(event):
    quit()

class NoteWindow(wx.Frame):
    def __init__(self, parent, title):
        super(NoteWindow, self).__init__(parent, title=title,
                                      size=(800, 600))

        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        groupPanelSizer = wx.BoxSizer(wx.VERTICAL)
        notePanelSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(mainSizer)

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

        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnExit)
        wx.EVT_MENU(self, wx.ID_OPEN, self.OnOpen)
        wx.EVT_MENU(self, wx.ID_SAVE, self.OnSave)  # just "pass" in our demo
        wx.EVT_MENU(self, wx.ID_SAVEAS, self.OnSaveAs)

        #THIS IS TEMPORARY TEST CODE
        noteSizer = wx.BoxSizer(wx.HORIZONTAL)
        txt = wx.TextCtrl(self)
        chk = wx.CheckBox(self, wx.ID_ANY, "")
        btn = wx.Button(self, wx.ID_ANY, "Details")
        noteSizer.Add(chk, flag=wx.ALL, border=10)
        noteSizer.Add(txt, 1, flag=wx.EXPAND | wx.ALL, border=10)
        noteSizer.Add(btn, flag=wx.ALL, border=10)
        notePanelSizer.Add(noteSizer, flag= wx.EXPAND | wx.ALL, border=10)
        #END TEMPORARY TEST CODE

        self.buttons = []
        # Note - give the buttons numbers 1 to 6, generating events 301 to 306
        # because IB_BUTTON1 is 300
        for i in range(6):
            # describe a button
            bid = i + 1
            self.buttons.append(wx.Button(self, ID_BUTTON1 + i, "Button &" + str(bid)))
            # add that button to the sizer2 geometry
            groupPanelSizer.Add(self.buttons[i], flag = wx.ALL, border = 10)

        mainSizer.Add(groupPanelSizer, flag = wx.EXPAND)
        mainSizer.Add(notePanelSizer, 1, flag= wx.EXPAND)

        #Adds a button event listener to exit the program.
        self.Bind(wx.EVT_MENU, OnFrameExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_CLOSE, self.OnExit)


    def OnAbout(self):
        # A modal show will lock out the other windows until it has
        # been dealt with. Very useful in some programming tasks to
        # ensure that things happen in an order that  the programmer
        # expects, but can be very frustrating to the user if it is
        # used to excess!
        self.aboutme.ShowModal()  # Shows it
        # widget / frame defined earlier so it can come up fast when needed

    def OnExit(self, e):
        # A modal with an "are you sure" check - we don't want to exit
        # unless the user confirms the selection in this case ;-)
        #igot = self.doiexit.ShowModal()  # Shows it
        self.Close(True)  # Closes out this simple application
        sys.exit(0)

    def OnOpen(self, e):
        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()

            # Open the file, read the contents and set them into
            # the text edit window
            filehandle = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(filehandle.read())
            filehandle.close()

            # Report on name of latest file read
            self.SetTitle("Editing ... " + self.filename)
            # Later - could be enhanced to include a "changed" flag whenever
            # the text is actually changed, could also be altered on "save" ...
        dlg.Destroy()

    def OnSave(self, e):
        # Save away the edited text
        # Open the file, do an RU sure check for an overwrite!
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", \
                            wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be saved
            itcontains = self.control.GetValue()

            # Open the file for write, write, close
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            filehandle = open(os.path.join(self.dirname, self.filename), 'w')
            filehandle.write(itcontains)
            filehandle.close()
        # Get rid of the dialog to keep things tidy
        dlg.Destroy()

    def OnSaveAs(self, event):

        with wx.FileDialog(self, "Save XYZ file", wildcard="XYZ files (*.xyz)|*.xyz",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w') as file:
                    self.doSaveData(file)
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)


app = wx.App(False)
frame = NoteWindow(None, "Sample editor")
frame.Center()
app.MainLoop()

