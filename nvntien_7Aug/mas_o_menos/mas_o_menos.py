n = int(input("What is the result? "))
print("OK, let's begin\n")
for x in range(10, -1, -1):
    if x == 5:
        g = int(input("Your guess? (Half way done) "))
    elif x == 0:
        g = int(input("Your guess? (Last guess) "))
    else:
        g = int(input("Your guess? (" + str(x) + " left) "))

    if (n - g) > 50:
        print("It's way more")
    elif (n - g) <= 50 and (n - g) > 0:
        print("It's more")
    elif (n - g) < -50:
        print("It's way less")
    elif (n - g) >= -50 and (n - g) < 0:
        print("It's less")
    elif n == g:
        print("Congrats !")
        quit()
    if x == 0:
        if g != n:
            print("You lose :(")
