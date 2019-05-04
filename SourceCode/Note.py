import pymongo
import datetime

class note():

    def __init__(self, parent, userid, groupid, date, title = "", details = "", ischecked = False):

        self.userID = userid
        self.groupID = groupid
        self.date = datetime.datetime(date)
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

