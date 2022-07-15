print("\nX's and O's by Dylan\n")
print("Instructions: Choose your position by using the numbers 1-9 (shown below).")

x_turn = -1
o_turn = -1
player = "X"
taken = []
won = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
grid = [" "] * 9
x_taken = []
o_taken = []
test = True
while (test):
    print("""   
       |   |
     1 | 2 | 3
    ___|___|___
       |   |
     4 | 5 | 6
    ___|___|___
       |   |
     7 | 8 | 9
       |   |""")
    choice = input("Choose a number 1-9 for where you want to play for player " + player + ": ")

    try:
        choice = int(choice)
    except:
        print("Not a valid number between 1-9")
        continue

    if (choice - 1) in taken:
        print("Sorry, that space is already taken. Choose again")
        continue
    else:
        taken.append(choice - 1)
        if (player == "X"):
            x_turn += 1
            x_taken.append(choice - 1)
        else:
            o_turn += 1
            o_taken.append(choice - 1)

    # Add the player's choice to the grid
    grid[choice - 1] = player

    print("""   
       |   |
     """ + grid[0] + """ | """ + grid[1] + """ | """ + grid[2] + """
    ___|___|___
       |   |
     """ + grid[3] + """ | """ + grid[4] + """ | """ + grid[5] + """
    ___|___|___
       |   |
     """ + grid[6] + """ | """ + grid[7] + """ | """ + grid[8] + """
       |   |""")

    # Check if the player has won
    for i in won:
        if player == "X":
            if (all(x in x_taken for x in i)):
                print(player, "won")
                test = False
                break
        else:
            if (all(x in o_taken for x in i)):
                print(player, "won")
                test = False
                break

    if player == "X":
        player = "O"
    else:
        player = "X"

    continue