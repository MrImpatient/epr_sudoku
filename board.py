from util.getch import getch

sd = {}

def init():
    global sd
    
    for row in range(9):
         for col in range(9):
                 sd[(row,col)] = 0

    #sd[2,1] = 5
    #sd[8,4] = 3

def plot():
    global sd
    
    print("\n\n")
    print("   ","  A   B   C   D   E   F   G   H   I")
    print("   ","*************************************")
    print(" 1 ","*",sd[0,0],"*",sd[0,1],"*",sd[0,2],"*",sd[0,3],"*",sd[0,4],"*",sd[0,5],"*",sd[0,6],"*",sd[0,7],"*",sd[0,8],"*")
    print("   ","*************************************")
    print(" 2 ","*",sd[1,0],"*",sd[1,1],"*",sd[1,2],"*",sd[1,3],"*",sd[1,4],"*",sd[1,5],"*",sd[1,6],"*",sd[1,7],"*",sd[1,8],"*")
    print("   ","*************************************")
    print(" 3 ","*",sd[2,0],"*",sd[2,1],"*",sd[2,2],"*",sd[2,3],"*",sd[2,4],"*",sd[2,5],"*",sd[2,6],"*",sd[2,7],"*",sd[2,8],"*")
    print("   ","*************************************")
    print(" 4 ","*",sd[3,0],"*",sd[3,1],"*",sd[3,2],"*",sd[3,3],"*",sd[3,4],"*",sd[3,5],"*",sd[3,6],"*",sd[3,7],"*",sd[3,8],"*")
    print("   ","*************************************")
    print(" 5 ","*",sd[4,0],"*",sd[4,1],"*",sd[4,2],"*",sd[4,3],"*",sd[4,4],"*",sd[4,5],"*",sd[4,6],"*",sd[4,7],"*",sd[4,8],"*")
    print("   ","*************************************")
    print(" 6 ","*",sd[5,0],"*",sd[5,1],"*",sd[5,2],"*",sd[5,3],"*",sd[5,4],"*",sd[5,5],"*",sd[5,6],"*",sd[5,7],"*",sd[5,8],"*")
    print("   ","*************************************")
    print(" 7 ","*",sd[6,0],"*",sd[6,1],"*",sd[6,2],"*",sd[6,3],"*",sd[6,4],"*",sd[6,5],"*",sd[6,6],"*",sd[6,7],"*",sd[6,8],"*")
    print("   ","*************************************")
    print(" 8 ","*",sd[7,0],"*",sd[7,1],"*",sd[7,2],"*",sd[7,3],"*",sd[7,4],"*",sd[7,5],"*",sd[7,6],"*",sd[7,7],"*",sd[7,8],"*")
    print("   ","*************************************")
    print(" 9 ","*",sd[8,0],"*",sd[8,1],"*",sd[8,2],"*",sd[8,3],"*",sd[8,4],"*",sd[8,5],"*",sd[8,6],"*",sd[8,7],"*",sd[8,8],"*")
    print("   ","*************************************")
    print("\n\n")

def save_to_file(file: str):
    import pickle
    global sd
    
    if file == "":
        file = "default.sav"

    filehandler = open(file,"wb")
    pickle.dump(sd, filehandler)
    filehandler.close()

def load_from_file(file: str):
    import pickle
    global sd

    if file == "":
        file = "default.sav"

    filehandler = open(file, "rb")
    sd = pickle.load(filehandler)
    filehandler.close()
