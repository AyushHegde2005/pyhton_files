import string


print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice_1 = input("You're at a cross road. Where do you want to go?\n Type 'left' or 'right':\n").lower()
if 'left' == choice_1:
     print("\nYou have to come to a lake. There is an island in the middle of the lake.")
     choice_2 = input("Type 'wait' to wait for a boat or type 'swim' to swim across.:\n").lower()
     if 'wait' == choice_2:
         print("\nYou arrive at the island unharmed. There is a house with 3 doors."
               "one red, one yellow and one blue, with treasure being behind one of these doors?")
         choice_3 = input("Which colour do you choose?\n").lower()
         if 'yellow' == choice_3:
             print("\ncongrats!! you have successfully found the treasure. You win!!")
         elif 'red' == choice_3:
             print("The room is full of fire. Game over!")
         elif 'blue' == choice_3:
             print("The room is full of poisonous snakes.Game over!")


     elif 'swim' == choice_2:
         print("There are crocodiles in the lake. \nGame over!")
     else:
         print("You have typed invalid character.")
elif 'right' == choice:
    print("Game over!")

else:
    print("You have typed invalid character.")
