from util.getch import getch

import board
import command

gameboard = board.init()
board.plot(gameboard)

game = True

while (game == True):

    userstring = input("Geben Sie einen Befehl ein: ").lower()

    b = command.parser(userstring)

    print(b)

    for i in range(len(b)):
        if b[i] in ("save", "s"):
            command.save_to_file(i, b, gameboard)
        elif b[i] in ("quit","exit", "q", "e"):
            game = False
        elif b[i] in ("load", "l"):
            temp = command.load_from_file(i,b)
            if temp != 0:
                gameboard = temp
        elif b[i] in ("update", "u"):
            board.plot(gameboard)
        else:
            if b[i] != "filename":
                print("Befehl ", b[i], " nicht gefunden!")


print("Bye!")

getch()
