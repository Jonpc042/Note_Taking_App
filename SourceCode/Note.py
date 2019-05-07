import pymongo
import datetime

class Note():

    def __init__(self, parent, userid=0, uniqueid=0, date=datetime.datetime.now(), title = "", details = "", ischecked = False):

        self.userID = userid
        self.uniqueID = uniqueid
        self.date = date
        self.title = title
        self.details = details
        self.isChecked = ischecked



    def toDocument(self) -> dict:
        mydict = {"UserID": self.userID,
                  "UniqueID": self.uniqueID,
                  "Date": self.date,
                  "Title": self.title,
                  "Details": self.details,
                  "IsChecked": self.details}
        return mydict

    def fromDocument(cls, dict):
        userid = dict.get('UserID')
        uniqueid = dict.get('UniqueID')
        date = dict.get('Date')
        title = dict.get('Title')
        details = dict.get('Details')
        ischecked = dict.get('IsChecked')
        return cls(userid, uniqueid, date, title, details, ischecked)

