#This program calculates the total bill including the tip and the price each person has to pay
print("Welcome to the tip calculator!")

#First we take the actuall bill amount
bill = int(input("What was the total bill?  Rs."))

#then we take the percentage of tip the costomer wants to pay
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))

#Then we input the number of people who would share the bill cost
no_of_people = int(input("How many people to split the bill"))

#Then we calculate the total cost and the price each person has to pay
bill += (12/100)*bill
cost_per_person = bill / no_of_people

#And then we output the results using f-strings
print(f"The total cost would be Rs.{round(bill, 2)} and each person should pay Rs.{round(cost_per_person, 2)}")


