from util.getch import getch

import board
import command

board.init()
board.plot()

game = True

while (game == True):

    userstring = input("Geben Sie einen Befehl ein: ")

    b = command.parser(userstring)

    print(b)

    for i in range(len(b)):
        if b[i] == "save":
            if (i+1) < len(b):
                file = b[i+1] + ".sav"
                print("Board gespeichert unter ", file)
            else:            
                file =''
                print("Board gespeichert unter default.sav")
            board.save_to_file(file)
        if b[i] in ("quit","exit", "q", "e"):
            game = False
        if b[i] == "load":
            if (i+1) < len(b):
                file = b[i+1] + ".sav"
                print("Board geladen von ", file)
            else:            
                file =''
                print("Board geladen von default.sav")
            board.load_from_file(file)
        if b[i] in ("update", "u"):
            board.plot()


print("Bye!")

getch()
