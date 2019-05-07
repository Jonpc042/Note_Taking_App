#!/usr/bin/env python
import wx
import sys
import pymongo
import MyPanel
import Note
from bson.objectid import ObjectId

def OnFrameExit(event):
    quit()

def ask(parent=None, message='', value=''):
    dlg = wx.TextEntryDialog(parent, message, value="")
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    return result


class Note_Window(wx.Frame):

    def __init__(self, parent, title, username):
        super(Note_Window, self).__init__(parent, title=title,
                                      size=(800, 600))

        self.username = username
        self.client = pymongo.MongoClient(
            "mongodb+srv://Jonpc042:SomePassword2019@cluster0-or0xk.mongodb.net/test?retryWrites=true")

        self.db = self.client["NoteAppDataBase"]
        self.usersCol = self.db["UserCollection"]
        self.notesCol = self.db["NoteCollection"]

        btn = wx.Button(self, wx.ID_NEW, "New Note")
        wx.EVT_BUTTON(self, wx.ID_NEW, self.OnNew)


        self.myNotes = []
        myquery = {"UserID": self.username}
        for x in self.notesCol.find(myquery):
            note = Note.Note(self)
            note.fromDocument(x)
            self.myNotes.append(note)
            print("Added Note: " + note.title.GetLabelText())

        self.mainClient = parent
        self.number_of_buttons = 0

        print(self.username)

        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        #self.groupPanelSizer = wx.BoxSizer(wx.VERTICAL)
        note = Note.Note(self)
        note1 = Note.Note(self)
        note.title = "Note"
        note.isChecked = False
        note1.title = "Another Note"
        note1.isChecked = True
        note2 = Note.Note(self)
        note2.title = "A third Note"
        note2.isChecked = False
        note3 = Note.Note(self)
        note3.title = "A fourth Note"
        note3.isChecked = True
        #self.myNotes.append(note)
        #self.myNotes.append(note1)
        #self.myNotes.append(note2)
        #self.myNotes.append(note3)

        self.notePanelSizer = wx.BoxSizer(wx.VERTICAL)
        self.notePanelSizer.Add(btn, flag=wx.ALL, border=10)
        self.notePanelSizer = self.buildNotePanel(self.notePanelSizer, self.myNotes)
        self.SetSizer(self.mainSizer)

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

        self.menuBar = wx.MenuBar()
        self.menuBar.Append(filemenu,"&File")
        self.SetMenuBar(self.menuBar)
        self.Show(True)

        #wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        #wx.EVT_MENU(self, wx.ID_EXIT, self.OnExit)
        #wx.EVT_MENU(self, wx.ID_OPEN, self.OnOpen)
        #wx.EVT_MENU(self, wx.ID_SAVE, self.OnSave)
        #wx.EVT_MENU(self, wx.ID_SAVEAS, self.OnSaveAs)

        #self.newgrpbut = wx.Button(self, size=(150,-1), label = "Add new Group")

        #self.groupPanelSizer.Add(self.newgrpbut, flag = wx.ALL, border = 10)

        #self.newgrpbut.Bind(wx.EVT_BUTTON, self.newgroup_clicked)

        #self.buttons = []
        # Note - give the buttons numbers 1 to 6, generating events 301 to 306
        # because IB_BUTTON1 is 300
        #for i in range(6):
            # describe a button
        #    bid = i + 1
        #    self.buttons.append(wx.Button(self, ID_BUTTON1 + i, "Button &" + str(bid)))
            # add that button to the sizer2 geometry
        #    groupPanelSizer.Add(self.buttons[i], flag = wx.ALL, border = 10)

        #self.mainSizer.Add(self.groupPanelSizer, flag = wx.EXPAND)
        self.mainSizer.Add(self.notePanelSizer, 1, flag= wx.EXPAND)

        #Adds a button event listener to exit the program.
        #self.Bind(wx.EVT_MENU, OnFrameExit, id=wx.ID_EXIT)
        #self.Bind(wx.EVT_CLOSE, self.OnExit)

    def newgroup_clicked(self, event):
        # When new group button is clicked, create a new group and place group button underneath
        groupname = ask(message='Please name your new group of notes')

        self.number_of_buttons += 1

        self.label = groupname
        self.name = groupname

        self.new_button = wx.Button(self, label=self.label, size=(150,-1), name=self.name)

        #self.new_button.Bind(self, wx.EVT_BUTTON, self.groupbutton_clicked)

        self.groupPanelSizer.Add(self.new_button, 0, wx.ALL, 5)

        self.mainSizer.Layout()
        self.groupPanelSizer.Layout()
        self.notePanelSizer.Layout()
        self.new_button.Layout()

        self.frame.Fit()
        self.groupPanelSizer.Fit()
        self.mainSizer.Fit()
        self.notePanelSizer.Fit()
        self.new_button.Fit()

        #myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        #mydb = myclient["Notepad"]
        #mycol = mydb["notes"]

        #mydict = {"userid": username, "groupid": groupname, "date": datetime, "title": title, "details": note_body, "ischecked": strike_thru}

        #x = mycol.insert_one(mydict)

    def delete_group(self, event):
        if self.groupPanelSizer.GetChildren():
            self.groupPanelSizer.Hide(self.number_of_buttons-1)
            self.groupPanelSizer.Remove(self.number_of_buttons-1)
            self.number_of_buttons -= 1
            self.groupPanelSizer.Layout()
            self.notePanelSizer()
            self.groupPanelSizer.Fit()

    def groupbutton_clicked(self, event):
        z = False

    def OnNew(self, e):
        #add a new note
        note = Note.Note(self)
        sizer = self.buildNote(note)
        self.notePanelSizer.Add(sizer, flag=wx.EXPAND | wx.ALL, border=10)
        self.notePanelSizer.Layout()

    def save_clicked(self, event):
        print("Save was clicked!")

        note = event.GetEventObject().GetParent()
        mydict = note.toDocument()
        query = {"_id" : mydict.get("_id")}
        update = { "$set": mydict}
        self.notesCol.update_one(query, update, upsert=True)

    def get_user(self, user):
        self.username = user

    def getNotes(self):
        #get some notes
        for i in range(0, 6):
            print(i)

    def buildNote(self, note):
        noteSizer = wx.BoxSizer(wx.HORIZONTAL)

        note.btn.Bind(wx.EVT_BUTTON, self.save_clicked)
        noteSizer.Add(note.isChecked, flag=wx.ALL, border=10)
        noteSizer.Add(note.title, 1, flag=wx.EXPAND | wx.ALL, border=10)
        noteSizer.Add(note.btn, flag=wx.ALL, border=10)
        print("built note: " + note.title.GetLabelText())
        return noteSizer

    def buildNotePanel(self, sizerPanel, notes):
        for note in notes:
            sizer = self.buildNote(note)
            sizerPanel.Add(sizer, flag=wx.EXPAND | wx.ALL, border=10)
        return sizerPanel



#app = wx.App(False)
#frame = NoteWindow(None, "Sample editor")
#frame.Center()
#app.MainLoop()

def main(self):
    app = wx.App()
    view = Note_Window()
    view.main()
    app.mainLoop()

if __name__ == "__main__":
     main()