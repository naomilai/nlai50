# Naomi Lai
# UWSD
# SoftDev
# K06 -- The More You Know About Your Data
# 2024-9-19
# time spent: 0.5

'''
DISCO:
...
QCC:
...
HOW THIS SCRIPT WORKS:
    read_csv turns the data in occupations.csv into a dictionary where the key is the percentage, and the value is the occupation.
    choose_random takes the dictionary of percent/occupation and chooses a random percent. It loops through the keys until the percentage aligns.
...
'''

import csv
import random

def read_csv(csvfile):
    with open(csvfile, newline='') as csv_file:
        header = next(csv_file)
        percent = 0.0
        content = csv.reader(csv_file)
        dic = {}
        for row in content:
            percent += float(row[1])
            percent = round(percent, 1)
            dic[percent] = row[0]

        dic.popitem()
        #print(dic) key: value --> percentage: occupation
        return dic
    
def choose_random(csvfile):
    data = read_csv(csvfile)
    keys = [key for key in data.keys()]
    random_num = random.random() * 99.8 #random_num is the chance
    for i in range(len(keys)):
        if keys[i] > random_num:
            return data[keys[i-1]] #when percentage is greater than random_num, it is the right occupation
    
print(choose_random('occupations.csv'))