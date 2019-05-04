from typing import Dict, Any, Union

import pymongo
import datetime


class note():

    def __init__(self, parent, title, userid, emailaddress, password):
        self.userID = userid
        self.emailAddress = emailaddress
        self.passwordSalt = ""
        self.hashedPassword = ""

    def __init__(self, userDict):
        self.userID =

    def toDocument(self) -> dict:
        mydict = {"UserID": self.userID,
                  "Email": self.emailAddress,
                  "Salt": self.passwordSalt,
                  "Hash": self.hashedPassword}
        return mydict

