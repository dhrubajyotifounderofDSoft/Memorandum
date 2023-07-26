import random
import os
import time

time.sleep(2)
words = ["quantum computer", "super computer", "personal computer"]
words.sort()
sorted_list = sorted(words)
print(sorted_list)
time.sleep(10)
os.system('cls')
num = 0
user_input_list = []

'''
For printing the input fields from user and appending them in a list
'''
for num in range(1,4):
    user_input_list.append(input(f"Write word {num} : "))
        
user_input_list.sort()
user_input_list_sorted = sorted(user_input_list)


# print(user_input_list)
# print(user_input_list_sorted)


if (words == user_input_list_sorted):
    print("You are correct! You won!🎉")
else:
    print("You are wrong!You are defeated")
    print("These are the actual words: \n")
    print(words)