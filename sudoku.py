from util.getch import getch

import board
import command

board.init()
board.plot()

b = command.parser(" test1 test2 ")

print(b)

getch()
