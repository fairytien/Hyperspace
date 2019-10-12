size = int(input())
if size <= 0:
    print("Invalid value")
characters = input()
if size > 1:
    print(characters[0], characters[1] * (size - 2), characters[0], sep='')
    for x in range(size - 2):
        print(characters[3], " " * (size - 2), characters[4], sep='')
    print(characters[0], characters[2] * (size - 2), characters[0], sep='')
elif size == 1:
    print(characters[0])
