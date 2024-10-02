# peaches & mangoes: Anastasia Lee, Nia Lam, Naomi Lai
# SoftDev
# Sep 2024

import random
import csv
from flask import Flask, render_template
app = Flask(__name__)

d = {}
def randocc():
    percentages = []
    with open("data/occupations.csv", "r") as file:
        arr = list(csv.reader(file))[1:-2] #omit first and last lines
        #print(arr)
    for i in arr:
        d.update({i[0]:[float(i[1]), i[2]]})
        percentages.append(float(i[1]))
    d.update({"Ducky":[0.2,"https://www.peta.org/features/facts-about-ducks/"]}) #make the total 100%
    percentages.append(0.2)
    # print(len(percentages))
    # print(len(list(d.keys())))
    random_occ = random.choices(list(d.keys()), list(percentages))[0]
    return random_occ

# print(randocc())

@app.route("/")

@app.route("/wdywtbwygp")
def test_tmplt():
    return render_template('tablified.html',
                           foo = "random occupations generator",
                           rand = randocc(),
                           dictionary = d)


if __name__ == "__main__":
    app.debug = True
    app.run()