import random

choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors."))
print("You choose:")
if 0 == choice:
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)

    rock
    ''')
elif 1 == choice:
    print('''
         _______
     ---'   ____)____
               ______)
               _______)
              _______)
     ---.__________)
    
     paper
    ''')
elif 2 == choice:
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
     
     scissors
    ''')
else:
    print("You have typed wrong number.")

if 0 == choice or 1 == choice or 2 == choice:
    comp_choice = random.randint(0, 2)
    print("computer choose:")
    if 0 == comp_choice:
        print('''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)

        rock
        ''')
    elif 1 == comp_choice:
        print('''
            _______
        ---'   ____)____
                  ______)
                  _______)
                _______)
        ---.__________)

        paper
        ''')

    elif 2 == comp_choice:
        print('''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)

        scissors
          ''')

    if choice == comp_choice:
        print("It's a draw!")
    elif 1 == choice and 0 == comp_choice:
        print("you win!")
    elif 2 == choice and 1 == comp_choice:
        print("Yow win!")
    elif 0 == choice and 2 == comp_choice:
        print("You win!")
    else:
        print("You loose")





