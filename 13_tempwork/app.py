# peaches & mangoes
# SoftDev
# Sep 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import random
import csv
from flask import Flask, render_template
app = Flask(__name__)

d = {}
def randocc():
    with open("data/occupations.csv", "r") as file:
        arr = list(csv.reader(file))[1:-2] #omit first and last lines
    for i in arr:
        d.update({i[0]:float(i[1])})
    d.update({"Ducky":0.2}) #make the total 100%
    random_occ = random.choices(list(d.keys()), list(d.values()))[0]
    return random_occ

@app.route("/")

# def hello_world():
#     txt = "Team 54<br>Anastasia, Mark, Brian<br>"
#     txt += "<h2> A random occupation is chosen: " + randocc() + "</h2><br><br>"
#     txt += "<h3>Here is the list of occupations and their percentages:</h3><br>"
#     for key, values in d.items():
#         txt += key + '<div align="center">' + str(values) + "</div> <br>"
#     return txt

@app.route("/wdywtbwygp")
def test_tmplt():
    
    return render_template('tablified.html',
                           foo = "random occupations generator",
                           rand = randocc(),
                           dictionary = d)


if __name__ == "__main__":
    app.debug = True
    app.run()

