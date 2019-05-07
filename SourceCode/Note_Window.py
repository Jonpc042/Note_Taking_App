#!/usr/bin/env python
import wx
import sys
import pymongo
import MyPanel
import Note
import datetime
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

        self.allmynotesizers = []
        self.allmynotes = []
        self.allmynotes_index = 0
        self.buttons = []
        self.tfields = []

        #client = pymongo.MongoClient(
            #"mongodb+srv://Jonpc042:SomePassword2019@cluster0-or0xk.mongodb.net/test?retryWrites=true")

        #db = client["NoteAppDataBase"]
        #usersCol = db["UserCollection"]
        #notesCol = db["NoteCollection"]

        myclient = pymongo.MongoClient("mongodb+srv://Jonpc042:SomePassword2019@cluster0-or0xk.mongodb.net/test?retryWrites=true")
        mydb = myclient["NoteAppDataBase"]
        mycol = mydb["NoteCollection"]

        btn = wx.Button(self, wx.ID_NEW, "New Note", size=(150, 30))
        self.newnoteSizer = wx.BoxSizer(wx.VERTICAL)
        self.newnoteSizer.Add(btn, 0, wx.CENTER)

        self.myNotes = []
        myquery = {"UserID": username}
        print(myquery)
        for mydoc in mycol.find(myquery, {"_id":1 , "Date": 1, "Title": 1 , "Details": 1, "IsChecked": 1}):
            newnote = Note.Note(self)
            newnote.uniqueID = mydoc.get("_id")
            newnote.date = mydoc.get("Date")
            newnote.title = mydoc.get("Title")
            newnote.details = mydoc.get("Details")
            newnote.isChecked = mydoc.get("IsChecked")
            self.myNotes.append(newnote)

        self.client = parent
        self.number_of_buttons = 0
        self.username = username

        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        #self.addnote = wx.Button(self.panel, wx.ID_ANY, label="add new note", size=(60, 30))
        #self.addnote.Bind(wx.EVT_BUTTON, self.addnote_clicked)

        self.notePanelSizer = self.buildNotePanel(self.myNotes)
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

        wx.EVT_MENU(self, wx.ID_EXIT, self.OnExit)

        self.mainSizer.Add(self.notePanelSizer, 1, flag= wx.EXPAND)
        self.mainSizer.Add(self.newnoteSizer, 1, flag= wx.EXPAND)

        #Adds a button event listener to exit the program.
        self.Bind(wx.EVT_MENU, OnFrameExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.Bind(wx.EVT_BUTTON, self.save_clicked)
        self.Bind(wx.EVT_BUTTON, self.addnote_clicked)

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

    def OnExit(self, e):
        # A modal with an "are you sure" check - we don't want to exit
        # unless the user confirms the selection in this case ;-)
        #igot = self.doiexit.ShowModal()  # Shows it
        self.Close(True)  # Closes out this simple application
        sys.exit(0)

    def get_user(self, user):
        self.username = user

    def save_clicked(self, event):
        print("doingsomething!")
        thenewtext = ""
        theid = str(event.GetEventObject().myname)

        print(self.buttons.index(event.GetEventObject()))
        num = self.buttons.index(event.GetEventObject())
        print(self.tfields[num])
        tmp = self.tfields[num]
        thenewtext = tmp.GetValue()

        print(thenewtext)
        myclient = pymongo.MongoClient("mongodb+srv://Jonpc042:SomePassword2019@cluster0-or0xk.mongodb.net/test?retryWrites=true")
        mydb = myclient["NoteAppDataBase"]
        mycol = mydb["NoteCollection"]
        myquery = {"UserID": self.username}

        print("doingsomething2")
        for mydoc in mycol.find(myquery, {"_id": 1, "UserID": 1, "UniqueID": 1, "Date": 1, "Title": 1, "Details": 1, "IsChecked": 1}):
            print("doingsomething3")
            print(mydoc.get("_id"))
            print(theid)
            if str(mydoc.get("_id")) == theid:
                ob = ObjectId(theid)
                print("doingsomething4")
                mydict = {"UserID": mydoc.get("UserID"),
                          "UniqueID": theid,
                          "Date": mydoc.get("Date"),
                          "Title": thenewtext,
                          "Details": mydoc.get("Details"),
                          "IsChecked": mydoc.get("IsChecked")}
                #newvalues = {"$set": mydict}
                x = mycol.update_one({"_id": ObjectId(theid)},{'$set': mydict}, upsert=True)
                print("doingsomething5")
            else:
                print("Couldn't find the file")

    def getNotes(self):
        #get some notes
        for i in range(0, 6):
            print(i)

    def getupdatenotetext(self):
        val = self.txt.GetValue()
        return val

    def buildNote(self, note):
        buttonid = note.uniqueID
        inthetext = note.title
        noteSizer = wx.BoxSizer(wx.HORIZONTAL)
        txt = wx.TextCtrl(self)
        #txt.Bind(wx.EVT_TEXT, self.EvtText)
        txt.SetLabelText(note.title)
        txt.name = note.uniqueID
        txt.mytext = ""
        chk = wx.CheckBox(self, wx.ID_ANY, "")
        if note.isChecked == "True":
            chk.SetValue(True)
        elif note.isChecked == "False":
            chk.SetValue(False)
        btn = wx.Button(self, wx.ID_ANY, "Save")
        btn.myname = buttonid
        btn.Bind(wx.EVT_BUTTON, self.save_clicked)
        noteSizer.Add(chk, flag=wx.ALL, border=10)
        noteSizer.Add(txt, 1, flag=wx.EXPAND | wx.ALL, border=10)
        noteSizer.Add(btn, flag=wx.ALL, border=10)
        self.buttons.append(btn)
        self.tfields.append(txt)
        return noteSizer

    def EvtText(self, event):
        tempint = self.tfields.index(self)
        self.tfields[tempint].GetValue()

    def buildNotePanel(self, notes):
        sizerPanel = wx.BoxSizer(wx.VERTICAL)
        for note in notes:
            print("found note: " + note.title)
            sizer = self.buildNote(note)
            sizerPanel.Add(sizer, flag=wx.EXPAND | wx.ALL, border=10)
        return sizerPanel

    def addnote_clicked(self, event):
        myclient = pymongo.MongoClient("mongodb+srv://Jonpc042:SomePassword2019@cluster0-or0xk.mongodb.net/test?retryWrites=true")
        mydb = myclient["NoteAppDataBase"]
        mycol = mydb["NoteCollection"]

        #theid = str(event.GetEventObject().myname)

        mytime = datetime.datetime.now()

        print("ADD NOTE")

        mydict = {"UserID": self.username,
                  "UniqueID": "",
                  "Date": str(mytime.date()),
                  "Title": "",
                  "Details": "",
                  "IsChecked": "False"}
        x = mycol.insert_one(mydict)

        getback = mycol.find_one( {"UserID": self.username}, sort=[( "_id", pymongo.DESCENDING )])

        mydict = {"UserID": getback.get("UserID"),
                  "UniqueID": str(getback.get("_id")),
                  "Date": getback.get("Date"),
                  "Title": getback.get("Title"),
                  "Details": getback.get("Details"),
                  "IsChecked": getback.get("IsChecked")}
        x = mycol.update_one({"_id": ObjectId(getback.get("_id"))},{'$set': mydict}, upsert=True)
        note = Note.Note(self)
        note.uniqueID = getback.get("_id")
        note.date = getback.get("Date")
        note.title = getback.get("Title")
        note.details = getback.get("Details")
        note.isChecked = getback.get("IsChecked")
        self.myNotes.append(note)
        sizer = self.buildNote(note)
        self.notePanelSizer.Add(sizer, flag=wx.EXPAND | wx.ALL, border=10)
        self.notePanelSizer.Layout()
        #another = Note_Window.Note_Window(self, "Notes", self.username)


def main(self):
    app = wx.App()
    view = Note_Window()
    view.main()
    app.mainLoop()

if __name__ == "__main__":
     main()