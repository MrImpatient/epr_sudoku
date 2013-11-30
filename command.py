import pickle

def parser(command:str):
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

def save_to_file(i, b, sd):
    if (i+1) < len(b):
        #make sure that second argument is filename and not a command
        if b[i+1] not in ("quit", "q", "exit", "e", "update", "u"):
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
        print("Datei kann nicht angelegt werden!")
        return 0
    pickle.dump(sd, filehandler)
    filehandler.close()

def load_from_file(i, b):
    if (i+1) < len(b):
        #make sure that second argument is filename and not a command
        if b[i+1] not in ("quit", "q", "exit", "e", "update", "u"):
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
        print("Datei kann nicht geöffnet werden!")
        return 0
    sd = pickle.load(filehandler)
    filehandler.close()
    return sd
