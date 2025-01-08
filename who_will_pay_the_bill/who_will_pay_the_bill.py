import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
length_of_the_list = len(friends)

num = random.randint(0, length_of_the_list - 1)
print(f"The one who will pay the bill is {friends[num]}")

