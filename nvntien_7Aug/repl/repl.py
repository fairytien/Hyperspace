r = ""
while r != "quit":
    r = input("repl> ")
    if len(r) == 6:
        print("My length is 6")
    if r[0] == "a" or r[0] == "e" or r[0] == "i" or r[0] == "o" or r[0] == "u":
        for x in range(4):
            print(r[1:4], sep='')
    if r == "ls" or r == "cat" or r == "rev" or r == "pwd":
            print("I know the command", r, "!!")
    if r[0] == "0" and r[-1] != "9":
        for i in range(len(r)):
            if r[i] == '0' or r[i] == '1' or r[i] == '2' or r[i] == '3':
                print(r[i])
            elif r[i] == '4' or r[i] == '5' or r[i] == '6':
                print(r[i])
            elif r[i] == '7' or r[i] == '8' or r[i] == '9':
                print(r[i])
