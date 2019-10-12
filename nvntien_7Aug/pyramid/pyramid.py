size = int(input("What pyramid size do you want?\n"))
if size % 2 == 0:
    size = size - 1
if size % 2 == 1:
    for x in range(size - 1, -2, -2):
        print(" " * (x // 2), "#" * (size - x), sep='')
