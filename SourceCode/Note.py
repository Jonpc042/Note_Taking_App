import pymongo
import datetime
import wx
from bson.objectid import ObjectId

class Note(wx.Frame):

    def __init__(self, parent, userid=0, date=datetime.datetime.now(), title = "", details = "", ischecked = False):
        super(Note, self).__init__(parent, title=title)

        self.userID = userid
        self.uniqueID = ObjectId()
        self.date = date
        self.title = wx.TextCtrl(parent)
        self.title.SetLabelText(title)
        self.details = details
        self.isChecked = wx.CheckBox(parent)
        self.isChecked.SetValue(ischecked == True)
        self.btn = wx.Button(parent)
        self.btn.SetLabelText("Save")


    def toDocument(self) -> dict:
        mydict = {"_id" : self.uniqueID,
                  "UserID": self.userID,
                  "Date": self.date,
                  "Title": self.title.GetLabelText(),
                  "Details": self.details,
                  "IsChecked": str(self.isChecked.GetValue())}
        return mydict

    def fromDocument(self, dict):
        self.uniqueID = dict.get('_id')
        self.userID = dict.get('UserID')
        self.date = dict.get('Date')
        self.title.SetLabelText(dict.get('Title'))
        self.details = dict.get('Details')
        self.isChecked.SetValue(dict.get('IsChecked'))


