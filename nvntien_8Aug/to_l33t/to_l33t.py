newstring = ''


def to_l33t(string):
    global newstring
    for i in range(len(string)):
        if string[i].lower() == 'a':
            newstring = newstring + '4'
        elif string[i].lower() == 'e':
            newstring = newstring + '3'
        elif string[i].lower() == 'i':
            newstring = newstring + '1'
        elif string[i].lower() == 'o':
            newstring = newstring + '0'
        elif string[i].lower() == 'u':
            newstring = newstring + '8'
        else:
            newstring = newstring + string[i]
    return(newstring)
