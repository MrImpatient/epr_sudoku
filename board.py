from util.getch import getch

def init():

    sd = {}
    for row in range(9):
         for col in range(9):
                 sd[(row,col)] = 0

    return sd

def plot(sd):
    
    print("\n\n")
    print("""
     A   B   C   D   E   F   G   H   I
   +---+---+---+---+---+---+---+---+---+
 1 | {}   {}   {} | {}   {}   {} | {}   {}   {} |
   +           +           +           |
 2 | {}   {}   {} | {}   {}   {} | {}   {}   {} |
   +           +           +           |
 3 | {}   {}   {} | {}   {}   {} | {}   {}   {} |
   +---+---+---+---+---+---+---+---+---+
 4 | {}   {}   {} | {}   {}   {} | {}   {}   {} |
   +           |           +           |
 5 | {}   {}   {} | {}   {}   {} | {}   {}   {} |
   +           |           +           |
 6 | {}   {}   {} | {}   {}   {} | {}   {}   {} |
   +---+---+---+---+---+---+---+---+---+
 7 | {}   {}   {} | {}   {}   {} | {}   {}   {} |
   +           +           +           |
 8 | {}   {}   {} | {}   {}   {} | {}   {}   {} |
   +           +           +           |
 9 | {}   {}   {} | {}   {}   {} | {}   {}   {} |
   +---+---+---+-----------+-----------+
    """.format(sd[0,0], sd[0,1], sd[0,2], sd[0,3], sd[0,4], sd[0,5], sd[0,6], sd[0,7], sd[0,8],
               sd[1,0], sd[1,1], sd[1,2], sd[1,3], sd[1,4], sd[1,5], sd[1,6], sd[1,7], sd[1,8],
               sd[2,0], sd[2,1], sd[2,2], sd[2,3], sd[2,4], sd[2,5], sd[2,6], sd[2,7], sd[2,8],
               sd[3,0], sd[3,1], sd[3,2], sd[3,3], sd[3,4], sd[3,5], sd[3,6], sd[3,7], sd[3,8],
               sd[4,0], sd[4,1], sd[4,2], sd[4,3], sd[4,4], sd[4,5], sd[4,6], sd[4,7], sd[4,8],
               sd[5,0], sd[5,1], sd[5,2], sd[5,3], sd[5,4], sd[5,5], sd[5,6], sd[5,7], sd[5,8],
               sd[6,0], sd[6,1], sd[6,2], sd[6,3], sd[6,4], sd[6,5], sd[6,6], sd[6,7], sd[6,8],
               sd[7,0], sd[7,1], sd[7,2], sd[7,3], sd[7,4], sd[7,5], sd[7,6], sd[7,7], sd[7,8],
               sd[8,0], sd[8,1], sd[8,2], sd[8,3], sd[8,4], sd[8,5], sd[8,6], sd[8,7], sd[8,8]))
    print("\n\n")


