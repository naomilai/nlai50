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


d_list = []
d_percentage = []
def getPercentage(d_list):
    l = []
    for dic in d_list:
        l.append(dic.get('percentage'))
    # print(l)
    return l

def randocc():
    with open("data/occupations.csv", "r") as file:
        arr = list(csv.reader(file))[1:-1] #omit first and last lines
    for i in arr:
        d = {}
        d.update({"occupation":i[0]})
        d.update({"percentage":float(i[1])})
        d.update({"link":i[2]})
        #d.update({i[0]:float(i[1])})
        #print(d)
        #print("/n")
        d_list.append(d)
    #d.update({"Ducky":0.2}) #make the total 100%
    #print(d)
    d_percentage = getPercentage(d_list)

    random_occ = random.choices(d_list, d_percentage)[0]
    return random_occ.get('occupation')

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
                           dictionary = d_list)


if __name__ == "__main__":
    app.debug = True
    app.run()