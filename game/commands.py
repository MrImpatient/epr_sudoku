__author__ = "1224270: Frank Kramer, 3402993: Sascha Reynolds"
__version__ = "1.0"
__email__ = "frkramer@stud.uni-frankfurt.de, sreynold@stud.uni-frankfurt.de"

import pickle
from game.board import Board
from util.getch import getch

class Commands(object):
    """class that contains the functions
    to convert the user input to internal commands
    """
    def __init__(self):
        self.board = Board()
        self.gameboard = self.board.return_board()
        self.ignoreit = False
        pass
       
    def parser(self, command:str):
        """ Hacks the user-string into substrings
        >>> t.parser("test1 test2 -1.723434")
        ['test1', 'test2', '-1.723434']
        """
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
        """saves the gameboard (sd) into to a
        binary file. In case the user submits
        no name the file name is default.sav. If
        the user provides a name, the data is
        written in name.sav. "i" is the index
        of the save-command in the command-string "b"
        """
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
            print("\n----------------------------------------")
            print("\n  Bord gespeichert unter", file,"\n")
            print("----------------------------------------\n")
        except IOError:
            print("\n-----------------------------------------------")
            print("\n  Datei", file,"kann nicht angelegt werden! \n")
            print("-----------------------------------------------\n")
            return 0
        pickle.dump(sd, filehandler)
        filehandler.close()

    def load_from_file(self, i, b):
        """loads the gameboard from a
        binary file. In case the user submits
        no name the file name is default.sav. If
        the user provides a name, the routine is
        looking for a file in name.sav.
        "i" is the index of the save-command in
        the command-string "b"
        """
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
        """
        adds one number or several numbers to the gameboard.
        Format is "a(dd) YXValue" or "a(dd) X1Y1Value1 X2Y2Value2 ..."
        >>> sd = {}
        >>> for row in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
        ...    for col in range(1,10):
        ...         sd[(row,col)] = " "
        >>> t.ignoreit = True #if False doctest hangs endless at getchar()
        >>> t.add(sd,['a51'])
        'done'
        >>> t.add(sd,['aaa'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Reihe (1 - 9) bitte benennen! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.add(sd,['111'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Spalte (A - I) bitte benennen! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.add(sd,['b10'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Zahl muss zwischen 1 und 9 liegen! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.add(sd,['11'])
        <BLANKLINE>
        -----------------------------------------------------------
        <BLANKLINE>
           Bitte nach add DREI Zeichen angeben: SpalteZeileWert 
        <BLANKLINE>
        -----------------------------------------------------------
        <BLANKLINE>
        0
        """
        for x in command: 
            if len(x) == 3:
                #error check
                if x[0] not in ("a b c d e f g h i"):
                    print("\n------------------------------------------")
                    print("\n   Spalte (A - I) bitte benennen! \n")
                    print("------------------------------------------\n")
                    if self.ignoreit == False:
                        getch()
                    return 0
                elif x[1] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Reihe (1 - 9) bitte benennen! \n")
                    print("------------------------------------------\n")
                    if self.ignoreit == False:
                        getch()
                    return 0
                elif x[2] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Zahl muss zwischen 1 und 9 liegen! \n")
                    print("------------------------------------------\n")
                    
                    if self.ignoreit == False:
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
                        if self.ignoreit == False:
                            getch()
                        return 0
            else:
                print("\n-----------------------------------------------------------")
                print("\n   Bitte nach add DREI Zeichen angeben: SpalteZeileWert \n")
                print("-----------------------------------------------------------\n")
                if self.ignoreit == False:
                        getch()
                return 0
        if self.ignoreit == False:
            return gameboard
        else:
            return "done"   #special flag for doctest to avaid return full gameboard

    def delete(self, gameboard, command):
        """
        deletes a number from the gameboard.
        Format is "d(elete) YX"
        >>> sd = {}
        >>> for row in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
        ...    for col in range(1,10):
        ...         sd[(row,col)] = " "
        >>> t.ignoreit = True #if False doctest hangs endless at getchar()
        >>> t.delete(sd,['aa'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Reihe (1 - 9) bitte benennen! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.delete(sd,['11'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Spalte (A - I) bitte benennen! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.delete(sd,['111'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Bitte nach delete ZWEI Zeichen angeben! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.delete(sd,['a1'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Das Feld ist schon leer! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.add(sd,['a51'])
        'done'
        >>> t.delete(sd,['a5'])
        'done'
        """
        for x in command:
            if len(x) == 2:
                #error check
                if x[0] not in ("a b c d e f g h i"):
                    print("\n------------------------------------------")
                    print("\n   Spalte (A - I) bitte benennen! \n")
                    print("------------------------------------------\n")
                    if self.ignoreit == False:
                        getch()
                    return 0
                elif x[1] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Reihe (1 - 9) bitte benennen! \n")
                    print("------------------------------------------\n")
                    if self.ignoreit == False:
                        getch()
                    return 0
                elif gameboard[x[0],int(x[1])] != " ":
                    gameboard[x[0],int(x[1])] = " "
                else:
                    print("\n------------------------------------------")
                    print("\n   Das Feld ist schon leer! \n")
                    print("------------------------------------------\n")
                    if self.ignoreit == False:
                        getch()
                    return 0
            else:
                print("\n------------------------------------------")
                print("\n   Bitte nach delete ZWEI Zeichen angeben! \n")
                print("------------------------------------------\n")
                if self.ignoreit == False:
                        getch()
                return 0
        if self.ignoreit == False:
            return gameboard
        else:
            return "done" 

    def change(self, gameboard, command):
        """
        adds one number or several numbers to the gameboard.
        Format is "a(dd) YXValue" or "a(dd) X1Y1Value1 X2Y2Value2 ..."
        >>> sd = {}
        >>> for row in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
        ...    for col in range(1,10):
        ...         sd[(row,col)] = " "
        >>> t.ignoreit = True #if False doctest hangs endless at getchar()
        >>> t.change(sd,['aaa'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Reihe (1 - 9) bitte benennen! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.change(sd,['111'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Spalte (A - I) bitte benennen! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.change(sd,['b10'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Zahl muss zwischen 1 und 9 liegen! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.change(sd,['11'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Bitte nach change DREI Zeichen angeben! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.change(sd,['b15'])
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
           Kann nur belegte Felder ändern! 
        <BLANKLINE>
        ------------------------------------------
        <BLANKLINE>
        0
        >>> t.add(sd,['a21'])
        'done'
        >>> t.change(sd,['a23'])
        'done'
        """
        for x in command:
            if len(x) == 3:
                #error check
                if x[0] not in ("a b c d e f g h i"):
                    print("\n------------------------------------------")
                    print("\n   Spalte (A - I) bitte benennen! \n")
                    print("------------------------------------------\n")
                    if self.ignoreit == False:
                        getch()
                    return 0
                elif x[1] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Reihe (1 - 9) bitte benennen! \n")
                    print("------------------------------------------\n")
                    if self.ignoreit == False:
                        getch()
                    return 0
                elif x[2] not in ("1 2 3 4 5 6 7 8 9"):
                    print("\n------------------------------------------")
                    print("\n   Zahl muss zwischen 1 und 9 liegen! \n")
                    print("------------------------------------------\n")
                    if self.ignoreit == False:
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
                    if self.ignoreit == False:
                        getch()
                    return 0
            else:
                print("\n------------------------------------------")
                print("\n   Bitte nach change DREI Zeichen angeben! \n")
                print("------------------------------------------\n")
                if self.ignoreit == False:
                        getch()
                return 0
                
        if self.ignoreit == False:
            return gameboard
        else:
            return "done" 
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'t': Commands()})
