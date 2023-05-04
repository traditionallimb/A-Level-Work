# <{Treasure Hunt game built on 3.10.5}>

# MODULES
# import prettytable [NOT INSTALLED]
import numpy as np




# Call up a menu for the user/player to pick either play or quit the program
def menu():
    loopCtrl = 1
    while loopCtrl == 1:        # Quality control of answer
        menuOp = int(input("1. Play\n2. Quit\n> "))
        loopCtrl = 2
        if menuOp == 1:
            return "Play"
        elif menuOp == 2:
            print("Quitting")
            quit()
        else:
            print("That isn't a valid answer, try again.")
            loopCtrl = 1


# Determine the position of the bandits and the treasure
def determine_positions():
    arrOps = ["B", "T", " "]
    board = np.random.choice(arrOps, size=(8,8), p=[0.078125,0.15625,0.765625])
    print(board)


        


            

start = menu()
if start == "Play":
    print("Playing")
    determine_positions()
