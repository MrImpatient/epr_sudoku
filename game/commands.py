import pickle

class Commands(object):
    def __init__(self):
        pass

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
        for i in command:
            if len(i) == 3:
                if (i[0], int(i[1])) in gameboard:
                    if gameboard[i[0],int(i[1])] == " ":
                        gameboard[i[0],int(i[1])] = i[2]
                    else:
                        print("Piece already set!")
                else:
                    print("Out of range!")
            else:
                print("Wrong syntax. Use '(a)dd RowColNumber'")
        return gameboard

    def delete(self, gameboard, command):
        for i in command:
            if len(i) == 2:
                if (i[0], int(i[1])) in gameboard:
                    if gameboard[i[0],int(i[1])] != " ":
                        gameboard[i[0],int(i[1])] = " "
                    else:
                        print("Spot is empty!")
                else:
                    print("Out of range!")
            else:
                print("Wrong syntax. Use '(d)elete RowCol'")
        return gameboard

    def change(self, gameboard, command):
        for i in command:
            if gameboard[i[0],int(i[1])] != " ":
                gameboard = delete(gameboard, [i[:-1]])
                gameboard = add(gameboard, [i])
            else:
                print("Can only change non empty spot.")
        return gameboard
