import pickle
from game.board import Board
from util.getch import getch

class Commands(object):
    def __init__(self):
        self.board = Board()
        self.gameboard = self.board.return_board()

    def parser(self, command:str):
        x = []
        temp = ''
        i = 0
        while i < (len(command)):
            while command[i] != " ":
                temp += command[i]
                i = i + 1
                if i == len(command):
                    break
            i = i + 1
            if temp != '':
                x.append(temp)
            temp = ''
        return x

    def save_to_file(self, i, b, sd):
        if (i+1) < len(b):
            #make sure that second argument is filename and not a command
            if b[i+1] not in ("quit", "q", "exit", "e", "refresh", "r"):
                if ".sav" not in b[i+1]:
                    file = b[i+1] + ".sav"
                    b[i+1] = "filename" #prevent double-use
                else:
                    file = b[i+1]
                    b[i+1] = "filename" #prevent double-use
            else:
                file = "default.sav"
        else:
            file = "default.sav"
        try:
            filehandler = open(file,"wb")
            print("Board gespeichert unter ", file)
        except IOError:
            print("Datei",file,"kann nicht angelegt werden!")
            return 0
        pickle.dump(sd, filehandler)
        filehandler.close()

    def load_from_file(self, i, b):
        if (i+1) < len(b):
            #make sure that second argument is filename and not a command
            if b[i+1] not in ("quit", "q", "exit", "e", "refresh", "r"):
                if ".sav" not in b[i+1]:
                    file = b[i+1] + ".sav"
                    b[i+1] = "filename" #prevent double-use
                else:
                    file = b[i+1]
                    b[i+1] = "filename" #prevent double-use
            else:
                file ="default.sav"
        else:
            file ="default.sav"
        sd = {}
        try:
            filehandler = open(file, "rb")
            print("Board geladen von ", file)
        except IOError:
            print("Datei",file, "kann nicht geöffnet werden!")
            return 0
        sd = pickle.load(filehandler)
        filehandler.close()
        return sd

    def add(self, gameboard, command):
        for x in command: #Variable darf keinen Spaltennamen haben!
            if len(x) == 3:
                #error check
                if x[0] not in ("a b c d e f g h i"):
                    print("Spalte muss zwischen A und I liegen!")
                    getch()
                    return gameboard
                elif x[1] not in ("1 2 3 4 5 6 7 8 9"):
                    print("Reihe muss zwischen 1 und 9 liegen!")
                    getch()
                    return gameboard
                elif x[2] not in ("1 2 3 4 5 6 7 8 9"):
                    print("Wert muss zwischen 1 und 9 liegen!")
                    getch()
                    return gameboard
                else:
                    if gameboard[x[0],int(x[1])] == " ":
                        legal = self.board.check_rules(gameboard,x[0],x[1],str(x[2]))
                        if legal:
                            gameboard[x[0],int(x[1])] = x[2]
                        else:
                            return 0
                    else:
                        print("Wert schon gesetzt! Change benutzen!")
                        getch()
                        return gameboard
            else:
                print("Bitte nach add DREI Zeichen angeben: SpalteZeileWert")
                getch()
        return gameboard

    def delete(self, gameboard, command):
        for x in command:
            if len(x) == 2:
                #error check
                if x[0] not in ("a b c d e f g h i"):
                    print("Spalte muss zwischen A und I liegen!")
                    getch()
                    return gameboard
                elif x[1] not in ("1 2 3 4 5 6 7 8 9"):
                    print("Reihe muss zwischen 1 und 9 liegen!")
                    getch()
                    return gameboard
                elif gameboard[x[0],int(x[1])] != " ":
                    gameboard[x[0],int(x[1])] = " "
                else:
                    print("Feld ist schon leer!")
                    getch()
            else:
                print("Bitte nach delete ZWEI Zeichen verwenden: SpalteZeile")
                getch()
        return gameboard

    def change(self, gameboard, command):
        for x in command:
            #error check
            if x[0] not in ("a b c d e f g h i"):
                print("Spalte muss zwischen A und I liegen!")
                getch()
                return gameboard
            elif x[1] not in ("1 2 3 4 5 6 7 8 9"):
                print("Reihe muss zwischen 1 und 9 liegen!")
                getch()
                return gameboard
            elif x[2] not in ("1 2 3 4 5 6 7 8 9"):
                print("Wert muss zwischen 1 und 9 liegen!")
                getch()
                return gameboard
            elif gameboard[x[0],int(x[1])] != " ":
                legal = self.board.check_rules(gameboard,x[0],x[1],str(x[2]))
                if legal:
                    self.gameboard = self.delete(gameboard, [x[:-1]])
                    self.gameboard = self.add(gameboard, [x])
                else:
                    return 0
            else:
                print("Kann nur gesetzte Felder ändern!")
                return 0
        return gameboard  
        
