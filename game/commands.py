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
            print("\nBoard gespeichert unter ", file,"\n")
        except IOError:
            print("\nDatei",file,"kann nicht angelegt werden!\n")
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
            print("\n----------------------------------------")
            print("\n  Spielfeld geladen aus", file,"\n")
            print("----------------------------------------\n")
        except IOError:
            print("\n---------------------------------------------------")
            print("\n  Datei", file,"kann nicht geöffnet werden!\n")
            print("---------------------------------------------------\n")
            return 0
        sd = pickle.load(filehandler)
        filehandler.close()
        return sd

    def add(self, gameboard, command):
        for x in command: #Variable darf keinen Spaltennamen haben!
            if len(x) == 3:
                #error check
                if x[0] not in ("a b c d e f g h i"):
                    print("\n------------------------------------------")
                    print("\n   Spalte (A - I) bitte benennen! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
                elif x[1] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Reihe (1 - 9) bitte benennen! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
                elif x[2] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Zahl muss zwischen 1 und 9 liegen! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
                else:
                    if gameboard[x[0],int(x[1])] == " ":
                        legal = self.board.check_rules(gameboard,x[0],x[1],str(x[2]))
                        if legal:
                            gameboard[x[0],int(x[1])] = x[2]
                        else:
                            return 0
                    else:
                        print("\n------------------------------------------")
                        print("\n   Zahl schon gesetzt! Change benutzen! \n")
                        print("------------------------------------------\n")
                        getch()
                        return 0
            else:
                print("\n-----------------------------------------------------------")
                print("\n   Bitte nach add DREI Zeichen angeben: SpalteZeileWert \n")
                print("----------------------------------------------------------\n")
                getch()
        return gameboard

    def delete(self, gameboard, command):
        for x in command:
            if len(x) == 2:
                #error check
                if x[0] not in ("a b c d e f g h i"):
                    print("\n------------------------------------------")
                    print("\n   Spalte (A - I) bitte benennen! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
                elif x[1] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Reihe (1 - 9) bitte benennen! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
                elif gameboard[x[0],int(x[1])] != " ":
                    gameboard[x[0],int(x[1])] = " "
                else:
                    print("\n------------------------------------------")
                    print("\n   Das Feld ist schon leer! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
            else:
                print("\n------------------------------------------")
                print("\n   Bitte nach delete ZWEI Zeichen angeben! \n")
                print("------------------------------------------\n")
                getch()
                return 0
        return gameboard

    def change(self, gameboard, command):
        for x in command:
            if len(x) == 3:
                #error check
                if x[0] not in ("a b c d e f g h i"):
                    print("\n------------------------------------------")
                    print("\n   Spalte (A - I) bitte benennen! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
                elif x[1] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Reihe (1 - 9) bitte benennen! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
                elif x[2] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Zahl muss zwischen 1 und 9 liegen! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
                elif gameboard[x[0],int(x[1])] != " ":
                    legal = self.board.check_rules(gameboard,x[0],x[1],str(x[2]))
                    if legal:
                        self.gameboard = self.delete(gameboard, [x[:-1]])
                        self.gameboard = self.add(gameboard, [x])
                    else:
                        return 0
                else:
                    print("\n------------------------------------------")
                    print("\n   Kann nur belegte Felder ändern! \n")
                    print("------------------------------------------\n")
                    getch()
                    return 0
            else:
                print("\n------------------------------------------")
                print("\n   Bitte nach change DREI Zeichen angeben! \n")
                print("------------------------------------------\n")
                getch()
                return 0
                
        return gameboard  
        
