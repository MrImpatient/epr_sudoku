from util.getch import getch
from util.clear_screen import clear_screen
def init():

    sd = {}
    for row in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
         for col in range(1,10):
                 sd[(row,col)] = " "
    return sd

def plot(sd):
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
    """.format(sd["a",1], sd["a",2], sd["a",3], sd["a",4], sd["a",5], sd["a",6], sd["a",7], sd["a",8], sd["a",9],
               sd["b",1], sd["b",2], sd["b",3], sd["b",4], sd["b",5], sd["b",6], sd["b",7], sd["b",8], sd["b",9],
               sd["c",1], sd["c",2], sd["c",3], sd["c",4], sd["c",5], sd["c",6], sd["c",7], sd["c",8], sd["c",9],
               sd["d",1], sd["d",2], sd["d",3], sd["d",4], sd["d",5], sd["d",6], sd["d",7], sd["d",8], sd["d",9],
               sd["e",1], sd["e",2], sd["e",3], sd["e",4], sd["e",5], sd["e",6], sd["e",7], sd["e",8], sd["e",9],
               sd["f",1], sd["f",2], sd["f",3], sd["f",4], sd["f",5], sd["f",6], sd["f",7], sd["f",8], sd["f",9],
               sd["g",1], sd["g",2], sd["g",3], sd["g",4], sd["g",5], sd["g",6], sd["g",7], sd["g",8], sd["g",9],
               sd["h",1], sd["h",2], sd["h",3], sd["h",4], sd["h",5], sd["h",6], sd["h",7], sd["h",8], sd["h",9],
               sd["i",1], sd["i",2], sd["i",3], sd["i",4], sd["i",5], sd["i",6], sd["i",7], sd["i",8], sd["i",9]))
    print("\n\n")


