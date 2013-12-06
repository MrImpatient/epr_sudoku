from util.getch import getch

from game.board import Board
from game.commands import Commands

class sudoku():
    def __init__(self):
        self.board = Board()
        self.gameboard = self.board.return_board()
        self.board.plot(gameboard = self.gameboard)
        self.command = Commands()

    def main(self):
        exit = False
        while exit is False:
            userstring = input("Geben Sie einen Befehl ein: ").lower()
            b = self.command.parser(userstring)

            for i in range(len(b)):
                if b[i] in ("save", "s"):
                    self.command.save_to_file(i, b, self.gameboard)
                elif b[i] in ("quit","exit", "q", "e"):
                    exit = True
                elif b[i] in ("load", "l"):
                    temp = self.command.load_from_file(i,b)
                    if temp != 0:
                        self.gameboard = temp
                elif b[i] in ("refresh", "r"):
                    self.board.plot(gameboard = self.gameboard)
                elif b[i] in ("add", "a"):
                    temp = self.command.add(self.gameboard, b[1:])
                    if temp != 0:
                        self.gameboard = temp
                        self.board.plot(gameboard = self.gameboard)
                elif b[i] in ("delete", "d"):
                    temp = self.command.delete(self.gameboard, b[1:])
                    if temp != 0:
                        self.gameboard = temp
                        self.board.plot(gameboard = self.gameboard)
                elif b[i] in ("change", "c"):
                    temp = self.command.change(self.gameboard, b[1:])
                    if temp != 0:
                        self.gameboard = temp
                        self.board.plot(gameboard = self.gameboard)
                else:
                    if b[i] != "filename":
                        b[i] = ""
                        #print("Befehl", b[i], "nicht gefunden!")

        print("\nBye!\n")
        getch()

if __name__ == "__main__":
    sudoku = sudoku()
    sudoku.main()
