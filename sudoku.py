from util.getch import getch

import board
import command

gameboard = board.init()
board.plot(gameboard)

game = True

while (game == True):

    userstring = input("Geben Sie einen Befehl ein: ").lower()

    b = command.parser(userstring)

    for i in range(len(b)):
        if b[i] in ("save", "s"):
            command.save_to_file(i, b, gameboard)
        elif b[i] in ("quit","exit", "q", "e"):
            game = False
        elif b[i] in ("load", "l"):
            temp = command.load_from_file(i,b)
            if temp != 0:
                gameboard = temp
        elif b[i] in ("refresh", "r"):
            board.plot(gameboard)
        elif b[i] in ("add", "a"):
            gameboard = command.add(gameboard, b[1:])

        else:
            if b[i] != "filename":
                print("Befehl", b[i], "nicht gefunden!")


print("Bye!")

getch()
