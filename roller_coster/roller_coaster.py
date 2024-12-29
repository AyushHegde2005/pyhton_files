print("welcome to the roller coaster ride!")

height = int(input("Please enter your height in cm :"))

if height >= 120:
    print("You are eligible to ride the roller coaster.")
    age = int(input("Enter your age:"))
    if 12 > age:
        print("The cost of your ticket will be Rs.100")
    elif 18 >= age:
        print("The cost of your ticket will be Rs.120")
    else:
        print("The cost of your ticket will be Rs.150")

else:
    print("Sorry, but you are not tall enough to ride the roller coaster.")

print("Thank You!!")
