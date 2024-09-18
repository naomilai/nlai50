# Naomi Lai
# peaches & mangoes
# SoftDev
# K<nn> -- <>
# <2024>-<09>-<17>
# time spent: <elapsed time in hours, rounded to nearest tenth>
import random
k = open('krewes.txt')
k_str = k.read()
# k.read() is a string
# print(k_str[0])
# list of dictionaries representing each devo
# each dictionary is of the form {<name>: [<period>, <ducky>}
k_list = k_str.split("@@@")
# k_list is a list of devos, with $$$ still included
# print(k_list)
k_list2 = []
for i in k_list:
info = i.split('$$$')
k_list2.append({info[1]:[info[0], info[2]]})
# k_list2 is a list of dictionaries, each one corresponding to a devo
# print(k_list2)
random_devo = random.choice(k_list2)
# randomly selected a devo
keys = random_devo.keys()
for key in keys:
print("Devo name: " + key)
values = random_devo.values()
for value in values:
print("Period: " + value[0])
print("Ducky name: " + value[1])
# prints random devo's name, period, and ducky name

