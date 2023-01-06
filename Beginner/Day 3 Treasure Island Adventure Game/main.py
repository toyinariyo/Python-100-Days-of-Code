print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
firstchoice = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'.\n").lower()
if firstchoice == "left":
    secondchoice = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait "
                         "for a boat or type 'swim' to swim across. \n").lower()
    if secondchoice == "wait":
        thirdchoice = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow"
                            "and one blue. Which colour do you choose? \n").lower()
        if thirdchoice == "red":
            print("This room is full of fire. Game over!")
        elif thirdchoice == "yellow":
            print("You found the treasure. You win!")
        elif thirdchoice == "blue":
            print("You enter a room full of piranhas. Game over!")
        else:
            print("This door doesn't exist. Game over!")
    else:
        print("You drowned. Game over!")
else:
    print("You fall into a sinkhole. Game over!")
