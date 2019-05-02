import pymongo
import datetime

class note():

    def __init__(self, parent, title, date):

        self.title = ""
        self.details = ""
        self.isChecked = False
        self.date = datetime.datetime(date)
