import string
print("Welcome to python pizza deliveries!")
choice = input("Would you like to order a pizza?\n").lower()
if "y" == choice:
    size = input("What size of pizza do you want? S(small), M(medium), or L(large):\n").lower()
    if 's' == size:
        bill = 199
    elif 'm' == size:
        bill = 299
    else:
        bill = 399

    extra_cheese = input("Do you want extra cheese? Y or N:\n").lower()
    if 'y' == extra_cheese:
        bill += 20

    peperoni = input("Do you want peperoni? Y or n N:\n").lower()
    if 'y'== peperoni:
        if 's' == size:
            bill += 40
        else:
            bill += 50

    print(f"\nYour choice of for pizza is as follow")
    print(f"Pizza=={size}\nextra cheese=={extra_cheese}\npeperoni=={peperoni}")
    print(f"The total bill price if Rs.{bill}")
    print("Thank you, please visit us again!")

else:
    print("sure no problem, thank you!")
