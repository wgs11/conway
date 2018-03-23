from random import randint
import copy
import time
import wx



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
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H")
        fileMenu.AppendSeparator()
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
        wx.MessageBox("This is a thing.","Another thing",wx.OK|wx.ICON_INFORMATION)


class Board():
    def print(self):
        output = ""
        for y in range(0, self.BOARDSIZE):
            output = output + str(self.board[y])+"\n"
        return output


    def create_board(self, size):
        self.board = [0] * size
        for y in range(0, size):
            self.board[y] = [0] * size

    def populate(self):
        for y in range(0, self.BOARDSIZE):
            for x in range(0, self.BOARDSIZE):
                self.board[y][x] = roll_spot()

    def __init__(self):
        self.BOARDSIZE = int(input("Enter Board Size: "))
        self.create_board(self.BOARDSIZE)
        self.populate()


def animate(board):
    tempboard = [0] * board.BOARDSIZE
    for y in range (0, board.BOARDSIZE):
        tempboard[y] = [0] * board.BOARDSIZE
    newcell = -1
    for y in range (0, board.BOARDSIZE):
        for x in range (0, board.BOARDSIZE):
            cell = board.board[y][x]
            neighbors = count_neighbors(board, y, x)
            if cell == 1 and neighbors < 2:
                newcell = 0
            elif cell == 1 and (2 <= neighbors <= 3):
                newcell = 1
            elif cell == 1 and neighbors > 3:
                newcell = 0
            elif cell == 0 and neighbors == 3:
                newcell = 1
            else:
                newcell = cell
            tempboard[y][x] = newcell
    time.sleep(2)
    board.board = tempboard
    return board


def count_neighbors(board, y, x):
    count = 0;
    for j in range (y - 1, y + 2):
        for i in range (x - 1, x + 2):
            if ((0 <= j < board.BOARDSIZE) and (0 <= i < board.BOARDSIZE)):
                if ((j != y) or (i != x)):
                    if board.board[j][i] == 1:
                        count += 1
    return(count)



def roll_spot():
    value = randint(0, 99)
    if value <= 30:
        return 1
    else:
        return 0

if __name__ == '__main__':
    app = wx.App()
    frm = AppFrame(None, title="Conway")
    frm.Show()
    app.MainLoop()





