# First things, first. Import the wxPython package.
import wx
import Login
import Note
import User

# We'll be handling files and directories, so we'll need this import
import os

# Set up some button numbers for the menu

class NoteAppClient:

    def __init__(self):

        self.loginWindow = Login.Login(self, self, "Login")
        self.loginWindow.main()


def main(self):
    app = wx.App()
    view = Login()
    view.main()
    app.mainLoop()

if __name__ == "__main__":
    main()