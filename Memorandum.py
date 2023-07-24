import random
import os

items = ["orange", "cashew", "banana"]
items.sort()
sorted_list = sorted(items)
num = 0
while (num < 3):
    num = num + 1
    # print(num)
    user_input = input(f"Write word {num} : ")
    user_input_list = [user_input]
print(user_input_list)

