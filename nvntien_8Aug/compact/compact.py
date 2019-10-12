array = []
newarray = []


def compact(array):
    for i in range(len(array)):
        if array[i] is not None:
            newarray.append(array[i])
    return(newarray)
