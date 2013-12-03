from util.clear_screen import clear_screen

class Board(object):
    def __init__(self):
        self.sd = {}
        for row in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
             for col in range(1,10):
                self.sd[(row,col)] = " "

    def return_board(self):
        return self.sd

    def plot(self, gameboard=None):
        if gameboard is not None:
            self.sd = gameboard
        clear_screen()
        print("\n\n")
        print("""
         1   2   3   4   5   6   7   8   9
       +---+---+---+---+---+---+---+---+---+
     A | {}   {}   {} | {}   {}   {} | {}   {}   {} |
       +           +           +           |
     B | {}   {}   {} | {}   {}   {} | {}   {}   {} |
       +           +           +           |
     C | {}   {}   {} | {}   {}   {} | {}   {}   {} |
       +---+---+---+---+---+---+---+---+---+
     D | {}   {}   {} | {}   {}   {} | {}   {}   {} |
       +           |           +           |
     E | {}   {}   {} | {}   {}   {} | {}   {}   {} |
       +           |           +           |
     F | {}   {}   {} | {}   {}   {} | {}   {}   {} |
       +---+---+---+---+---+---+---+---+---+
     G | {}   {}   {} | {}   {}   {} | {}   {}   {} |
       +           +           +           |
     H | {}   {}   {} | {}   {}   {} | {}   {}   {} |
       +           +           +           |
     I | {}   {}   {} | {}   {}   {} | {}   {}   {} |
       +---+---+---+-----------+-----------+
        """.format(self.sd["a",1], self.sd["a",2], self.sd["a",3], self.sd["a",4], self.sd["a",5], self.sd["a",6], self.sd["a",7], self.sd["a",8], self.sd["a",9],
                   self.sd["b",1], self.sd["b",2], self.sd["b",3], self.sd["b",4], self.sd["b",5], self.sd["b",6], self.sd["b",7], self.sd["b",8], self.sd["b",9],
                   self.sd["c",1], self.sd["c",2], self.sd["c",3], self.sd["c",4], self.sd["c",5], self.sd["c",6], self.sd["c",7], self.sd["c",8], self.sd["c",9],
                   self.sd["d",1], self.sd["d",2], self.sd["d",3], self.sd["d",4], self.sd["d",5], self.sd["d",6], self.sd["d",7], self.sd["d",8], self.sd["d",9],
                   self.sd["e",1], self.sd["e",2], self.sd["e",3], self.sd["e",4], self.sd["e",5], self.sd["e",6], self.sd["e",7], self.sd["e",8], self.sd["e",9],
                   self.sd["f",1], self.sd["f",2], self.sd["f",3], self.sd["f",4], self.sd["f",5], self.sd["f",6], self.sd["f",7], self.sd["f",8], self.sd["f",9],
                   self.sd["g",1], self.sd["g",2], self.sd["g",3], self.sd["g",4], self.sd["g",5], self.sd["g",6], self.sd["g",7], self.sd["g",8], self.sd["g",9],
                   self.sd["h",1], self.sd["h",2], self.sd["h",3], self.sd["h",4], self.sd["h",5], self.sd["h",6], self.sd["h",7], self.sd["h",8], self.sd["h",9],
                   self.sd["i",1], self.sd["i",2], self.sd["i",3], self.sd["i",4], self.sd["i",5], self.sd["i",6], self.sd["i",7], self.sd["i",8], self.sd["i",9]))
        print("\n\n")


