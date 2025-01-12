import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '$', '%', '&', '*', '(', ')', '-', '_']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

list_index = 0
print("********************************************************************************************************")
print("Welcome to the PyPassword Generator!".rjust(70))
print("********************************************************************************************************")

num_of_letters = int(input("How many letters would you like in your password?\n"))
list_index += num_of_letters

num_of_sym = int(input("How many symbols would you like in your password?\n"))
list_index += num_of_sym

num_of_numb = int(input("How many  numbers would you like in your password?\n"))
list_index += num_of_numb

list_of_char = [None]*list_index

for num in range(0, num_of_letters):
    list_of_char[num] = random.choice(letters)

for num in range(num_of_letters, num_of_letters + num_of_sym):
    list_of_char[num] = random.choice(symbols)

for num in range(num_of_letters + num_of_sym, num_of_letters + num_of_sym + num_of_numb):
    list_of_char[num] = random.choice(numbers)

random.shuffle(list_of_char)

print("The password is: ", end = "")
for char in list_of_char:
    print(char, end = "")

print("\n")
print("\n")
print("********************************************************************************************************")
