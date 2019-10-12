a = int(input("Value? "))
for x in range(a+1):
    if x != 0:
        if x % 5 == 0 and x % 9 != 0:
            print("In")
        elif x % 9 == 0 and x % 5 != 0:
            print("Tek")
        elif x % 45 == 0:
            print("InTek")
        else:
            print(x)
