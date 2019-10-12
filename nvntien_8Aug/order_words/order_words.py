array = []
def order_words(array):
    sorted(array)
    array1 = array
    for i in range(len(array)):
        newarray = [array[i]]
        for j in range(i + 1, len(array)):
            #if i < j:
                if len(array[i]) == len(array[j]):
                    newarray.append(array[j])
                    array1.pop(j)
        print(newarray)
        print(array1)

order_words(['aa', 'laurie', 'daniel', 'toto', 'tata', 'aA', 'AA', 'Aa'])
