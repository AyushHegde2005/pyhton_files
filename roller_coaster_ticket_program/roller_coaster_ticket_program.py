import string

print("welcome to the roller coaster ride!")
height = int(input("Please enter your height in cm :\n"))

if height >= 120:
    ticket_price = 0
    print("You are eligible to ride the roller coaster.")
    age = int(input("Enter your age:\n"))

    if 12 > age:
        ticket_price = 100
    elif 12 <= age <= 18:
        ticket_price = 120

    #we also include 'midlife crises(45 - 55)' in our program
    elif 45 <= age <= 55:
        ticket_price = 0
        print("Everthing is gonna be ok. Have a free ride on us!")
    else:
        ticket_price = 150

    #we ask the customer whether they want their photo's to be taken or not

    choice = input("Would you like your photos to be taken during the ride?Y or N\n").lower()
    if "y" == choice:
        ticket_price += 50
    print(f"Your total ticket price would be Rs.{ticket_price}")


else:
    print("Sorry, but you are not tall enough to ride the roller coaster.")

print("Thank You!!")
