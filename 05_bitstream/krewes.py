# Naomi Lai
# peaches & mangoes
# SoftDev
# K<nn> -- <>
# <2024>-<09>-<17>
# time spent: <elapsed time in hours, rounded to nearest tenth>


k = open('krewes.txt')

k_str = k.read()
#k.read() is a string
# print(k_str[0])

#list of dictionaries representing each period
#each period_dictionary contains items representing each devo
#each devo item is associated with a ducky value

# [4 = {anastasia: 'lily', devo2: 'ducky2'}, 5 = {}, 6 ={}]
#.split
k_list = k_str.split("@@@")
#k_list is a list

