from utility import roll_spot


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