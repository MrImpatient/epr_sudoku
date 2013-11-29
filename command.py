

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

