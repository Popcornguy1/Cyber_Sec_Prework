import string
import re


names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
even_list = []
odd__list = []


for x in names_list:
    if len(x) % 2  == 0: 
        even_list.append(x)
    else: 
        odd__list.append(x)

for z in range(len(even_list)):
    even_list[z] = 'b' + even_list[z][1:]
    

for y in range(len(odd__list)):
    odd__list[y] = 'c'+ odd__list[y][:-1]

print(even_list)

print(odd__list)