again = 'y'
while(again != 'n'):
    print("Rock Paper Scissors!")
    p1 = input("Player1: ").capitalize()
    p2 = input("Player2: ").capitalize()

    if p1.capitalize() != p2.capitalize():
        if p1.capitalize() == "scissors".capitalize():
            if p2.capitalize() == "rock".capitalize():
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
        if p1.capitalize() == "rock".capitalize():
            if p2.capitalize() == "scissors".capitalize():
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        if p1.capitalize() == "paper".capitalize():
            if p2.capitalize() == "scissors".capitalize():
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
    else:
        print("Tie!")

    again = input("Again? (y/n): ")
