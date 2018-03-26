from Board import *
import wx
from utility import *

class AppFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(AppFrame, self).__init__(*args, **kw)

        self.SetSize(500,500)
        self.makeMenuBar()

        pnl = wx.Panel(self, wx.ID_ANY)
        self.CreateStatusBar()
        self.SetStatusText("Conway")
        self.board = Board()
        self.st = wx.StaticText(pnl, label=self.board.print(), pos=(25, 25))
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.toggleBtn = wx.Button(pnl, wx.ID_ANY, "Start")
        self.toggleBtn.Bind(wx.EVT_BUTTON, self.onToggle)


    def onToggle(self, event):
        btnLabel = self.toggleBtn.GetLabel()
        if btnLabel == "Start":
            print ("starting timer")
            self.timer.Start(100)
            self.toggleBtn.SetLabel("Stop")
        else:
            print("stopped")
            self.timer.Stop()
            self.toggleBtn.SetLabel("Start")

    def update(self, event):
        self.board = animate(self.board)
        self.st.SetLabel(self.board.print())

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)


        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        self.Close(True)


    def OnAbout(self, event):
        wx.MessageBox("This is a thing.","Another thing",wx.OK|wx.ICON_INFORMATION)


