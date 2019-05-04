from typing import Dict, Any, Union

import pymongo
import datetime


class note():

    def __init__(self, parent, title, userid, emailaddress, password):
        self.userID = userid
        self.emailAddress = emailaddress
        self.passwordSalt = ""
        self.hashedPassword = ""

    def toDocument(self) -> dict:
        mydict = {"UserID": self.userID,
                  "Email": self.emailAddress,
                  "Salt": self.passwordSalt,
                  "Hash": self.hashedPassword}
        return mydict

    def fromDocument(cls, dict):
        userid = dict.get("UserID")
        emailaddress = dict.get("Email")
        salt = dict.get("Salt")
        hash = dict.get("Hash")
        return cls(userid, emailaddress, salt, hash)