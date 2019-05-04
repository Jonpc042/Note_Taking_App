import pymongo
import datetime

class note():

    def __init__(self, parent, title, userid, date, group):

        self.userID = userid
        self.group = group
        self.title = ""
        self.details = ""
        self.isChecked = False
        self.date = datetime.datetime(date)

    

    #def toDocument(self) -> dict:


