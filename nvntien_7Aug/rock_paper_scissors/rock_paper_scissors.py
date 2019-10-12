p1 = input("Player 1? ")
p2 = input("Player 2? ")

if (p1 == "rock" or p1 == "paper" or p1 == "scissors") and p1 == p2:
    print("Draw.")
elif p1 == "rock" and p2 == "paper":
    print("Player 2 wins.")
elif p1 == "paper" and p2 == "scissors":
    print("Player 2 wins.")
elif p1 == "scissors" and p2 == "rock":
    print("Player 2 wins.")
elif p2 == "rock" and p1 == "paper":
    print("Player 1 wins.")
elif p2 == "paper" and p1 == "scissors":
    print("Player 1 wins.")
elif p2 == "scissors" and p1 == "rock":
    print("Player 1 wins.")
else:
    print("Error.")
