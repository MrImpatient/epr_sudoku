__author__ = "1224270: Frank Kramer, 3402993: Sascha Reynolds"
__version__ = "1.0"
__email__ = "frkramer@stud.uni-frankfurt.de, sreynold@stud.uni-frankfurt.de"

from util.getch import getch
from util.clear_screen import clear_screen

from game.board import Board
from game.commands import Commands

class sudoku():
    def __init__(self):
        self.board = Board()
        self.gameboard = self.board.return_board()
        self.command = Commands()

    def main(self):
        """Main game loop. Collects user input
        and invokes internal commands to fulfill
        user commands.
        ->the commands are tested for input by
        doctest in command.py and board.py.
        """
        clear_screen()
        print("\n\n    A   B   C   D   E   F\n"
              "  +---+---+---+---+---+---+\n"
              "1 | S   U   D | O   K   U |\n"
              "  +           +           +\n\n\n"
              "'h' for help.")
        getch()
        clear_screen()
        exit = False
        self.board.plot(gameboard = self.gameboard)
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
                elif b[i] in ("help", "h"):
                    clear_screen()
                    f = open('help.txt', encoding="cp1252")
                    print(f.read())
                    f.close()
                    getch()
                    clear_screen()
                    self.board.plot(gameboard = self.gameboard)
                else:
                    if b[i] != "filename":
                        b[i] = ""
                        #print("Befehl", b[i], "nicht gefunden!")
        clear_screen()
        print("\nBye!\n")
        getch()
        clear_screen()

if __name__ == "__main__":
    sudoku = sudoku()
    sudoku.main()
