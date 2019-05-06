import wx
import pymongo
import hashlib
import random
import string

class Registration(wx.Frame):

    def __init__(self, parent, title):
        super(Registration, self).__init__(parent, title=title)
        wx.Frame.__init__(self, parent, title=title)
        self.panel = wx.Panel(self)
        self.client = parent

        self.loginfield = wx.TextCtrl(self.panel, size=(140, -1))
        self.logintitle = wx.StaticText(self.panel, label="Enter your username")
        self.emailfield = wx.TextCtrl(self.panel, size=(140, -1))
        self.emailtitle = wx.StaticText(self.panel, label="Enter your email address")
        self.passfield = wx.TextCtrl(self.panel, size=(140, -1), style=wx.TE_PASSWORD)
        self.passtitle = wx.StaticText(self.panel, label="Enter your password")
        self.passfieldverify = wx.TextCtrl(self.panel, size=(140, -1), style=wx.TE_PASSWORD)
        self.passtitleverify = wx.StaticText(self.panel, label="Verify your password")


        self.exitbutton = wx.Button(self.panel, label="Exit", pos=(130, 50), size=(60,30))
        self.registerbutton = wx.Button(self.panel, label="Register", pos=(130, 90), size=(60,30))
        self.exitbutton.Bind(wx.EVT_BUTTON, self.exit_clicked)
        self.registerbutton.Bind(wx.EVT_BUTTON, self.register_clicked)

        # Set sizer for the frame, so we can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.Add(self.logintitle, (0, 0))
        self.sizer.Add(self.loginfield, (1, 0))
        self.sizer.Add(self.emailtitle, (2, 0))
        self.sizer.Add(self.emailfield, (3, 0))
        self.sizer.Add(self.passtitle, (4, 0))
        self.sizer.Add(self.passfield, (5, 0))
        self.sizer.Add(self.passtitleverify, (6, 0))
        self.sizer.Add(self.passfieldverify, (7, 0))
        self.sizer.Add(self.registerbutton, (8, 0))
        self.sizer.Add(self.exitbutton, (9, 0))

        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        self.Show(True)

    def exit_clicked(event, e):
        print("Time to go!")
        quit()

    def register_clicked(self, e):
        self.Hide()

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Notepad"]
        mycol = mydb["users"]

        username = self.loginfield.GetValue()
        email = self.emailfield.GetValue()
        password = self.passfield.GetValue()
        passwordverify = self.passfieldverify.GetValue()


        if password == passwordverify:
            print("YAY! We registered successfully!")


            mystring = ""

            for int in range(30):
                mystring = mystring + (random.choice(string.printable))

            myhash = hashlib.sha512(( mystring + password).encode('utf-8')).hexdigest()

            mydict = { "username": username, "email": email, "password": myhash , "salt": mystring}

            x = mycol.insert_one(mydict)



        elif password != passwordverify:
            print("Registration Failed!")
            app = wx.App(False)
            frame = Registration(None, "Notekeeper!")
            frame.Center()
            frame.Show()
            app.MainLoop()

#app = wx.App(False)
#frame = Registration(None, "Notekeeper!")
#frame.Center()
#frame.Show()
#app.MainLoop()

def main(self):
    app = wx.App()
    view = Registration()
    view.main()
    app.mainLoop()

if __name__ == "__main__":
     main()