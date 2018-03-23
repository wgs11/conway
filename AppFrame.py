import wx



class AppFrame(wx.Frame):


    def __init__(self, *args, **kw):
        super(AppFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)

        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Conway")



    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H")
        exitItem = fileMenu.Append(wx.ID_EXIT)
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)


        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        self.Close(True)


    def OnHello(self, event):
        wx.MessageBox("Hello again.")


    def OnAbout(self, event):
        wx.MessageBox("This is a thing.",wx.OK|wx.ICON_INFORMATION)