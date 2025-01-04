print("Welcome to python pizza deliveries!")
print("Would you like to order a pizza?").lower
if 'y' == size:
    size = input("What size of pizza do you want? S(small), M(medium), or L(large):")
    if 's' == size or 'S' == size:
        bill = 199
    elif 'm' == size or 'm' == size:
        bill = 299
    else:
        bill = 399

    extra_cheese = input("Do you want extra cheese? Y or N:")
    if 'y' == extra_cheese or 'Y' == extra_cheese:
        bill += 20

    peperoni = input("Do you want peperoni? Y or n N:")
    if 'y'== peperoni or 'Y' == peperoni:
        if 's' == size or 'S' == size:
            bill += 40
        else:
            bill += 50

    print(f"\nYour choice of for pizza is as follow")
    print(f"Pizza=={size}\nextra cheese=={extra_cheese}\npeperoni=={peperoni}")
    print(f"The total bill price if Rs.{bill}")
    print("Thank you, please visit us again!"

else:
    print("sure no problem, thank you!")
