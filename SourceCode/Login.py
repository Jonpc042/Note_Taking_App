import wx
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Notepad"]

class Login(wx.Frame):
    def login_clicked(self, e):
        self.Hide()
        print("Button Pressed.")
        from Note_Window import NoteWindow

    def exit_clicked(event, e):
        print("Time to go!")
        quit()

    def register_clicked(self, e):
        self.Hide()
        print("Let's Register!")
        from Registration import Registration

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.panel = wx.Panel(self)
        self.loginfield = wx.TextCtrl(self.panel, size=(140, -1))
        self.logintitle = wx.StaticText(self.panel, label="Enter your username")
        self.passfield = wx.TextCtrl(self.panel, size=(140, -1), style=wx.TE_PASSWORD)
        self.passtitle = wx.StaticText(self.panel, label="Enter your password")

        self.loginbutton = wx.Button(self.panel, label="Login", pos=(130, 10), size=(60,30))
        self.exitbutton = wx.Button(self.panel, label="Exit", pos=(130, 50), size=(60,30))
        self.registerbutton = wx.Button(self.panel, label="Register", pos=(130, 90), size=(60,30))
        self.loginbutton.Bind(wx.EVT_BUTTON, self.login_clicked)
        self.exitbutton.Bind(wx.EVT_BUTTON, self.exit_clicked)
        self.registerbutton.Bind(wx.EVT_BUTTON, self.register_clicked)

        # Set sizer for the frame, so we can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.Add(self.logintitle, (0, 0))
        self.sizer.Add(self.loginfield, (1, 0))
        self.sizer.Add(self.passtitle, (2, 0))
        self.sizer.Add(self.passfield, (3, 0))
        self.sizer.Add(self.registerbutton, (4, 0))
        self.sizer.Add(self.loginbutton, (5, 0))
        self.sizer.Add(self.exitbutton, (6, 0))

        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

app = wx.App(False)
frame = Login(None, "Notekeeper!")
frame.Center()
frame.Show()
app.MainLoop()


#Code partially taken from https://stackoverflow.com/questions/14927584/simple-example-of-using-wx-textctrl-and-display-data-after-button-click-in-wxpyt
#by contributor Fenikso on 2/18/2013