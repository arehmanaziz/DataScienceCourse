print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print()

print("You're at a cross road.")
choice1 = input("Where do you want to go? (type: left/right) ").lower()


if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input(" Type 'wait' to wait for a boat -OR- Type 'swim' to swim across: ").lower()

    if choice2 == "wait":
        print("There are multiple doors.")
        choice3 = input("Which one to open? Type Red, Blue, Yellow, or any other color: ").lower()

        if choice3 == "red":
            print("You were burned by fire. GAME OVER.")

        elif choice3 == "blue":
            print("You were eaten by beasts. GAME OVER.")

        elif choice3 == "yellow":
            print("You Win!!")

        else:
            print("GAME OVER.")

            

    else:
        print("You were attacked by trout. GAME OVER.")



else:
    print("You have fall into a hole. GAME OVER.")

