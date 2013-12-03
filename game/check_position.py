__author__ = 'hnker'

def check_position(gameboard, position):
    for i in range(1,10):
        if i != position[1]:
            if gameboard[(position[0], i)] == position[2]:
                return False
    for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
        if i != position[0]:
            if gameboard[(i, int(position[1]))] == position[2]:
                return False

    return True
