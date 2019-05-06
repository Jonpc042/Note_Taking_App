import pymongo
import datetime

class Note():

    def __init__(self, parent, userid=0, groupid=0, date=datetime.datetime.now(), title = "", details = "", ischecked = False):

        self.userID = userid
        self.groupID = groupid
        self.date = date
        self.title = title
        self.details = details
        self.isChecked = ischecked



    def toDocument(self) -> dict:
        mydict = {"UserID": self.userID,
                  "GroupID": self.groupID,
                  "Date": self.date,
                  "Title": self.title,
                  "Details": self.details,
                  "IsChecked": self.details}
        return mydict

    def fromDocument(cls, dict):
        userid = dict.get('UserID')
        groupid = dict.get('GroupID')
        date = dict.get('Date')
        title = dict.get('Title')
        details = dict.get('Details')
        ischecked = dict.get('IsChecked')
        return cls(userid, groupid, date, title, details, ischecked)

