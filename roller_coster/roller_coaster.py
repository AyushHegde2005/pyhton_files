print("welcome to the roller coaster ride!")

height = int(input("Please enter your height in cm :"))

if height >= 120:
    print("You are eligible to ride the roller coaster.")
    age = int(input("Enter your age:"))
    if age >= 18:
        print("The cost of your ticket will be Rs.150")
    else:
        print("The cost of your ticket will be Rs.120")

else:
    print("Sorry, but you are not tall enough to ride the roller coaster.")

