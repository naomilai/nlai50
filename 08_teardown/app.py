# peaches & mangoes
# SoftDev
# K08 -- exploration with venv
# 2024-09-23
# time spent: 0.8 hours


'''
DISCO:
- create a venv with 'python3 -m venv <name>'
- activate with '. path/to/venv/bin/activate'
- use 'pip install flask' to install the flask package
- you need to run 'pip install flask' in the folder '<venv name>';
it will not work in the parent directory
- you can open links to websites from the terminal!
- deactivate venv using 'deactivate'


QCC:
0. I have seen somewhat similar syntax in import statements in java,
for packages and custom classes. Perhaps 'from flask import Flask'
is most similar to importing a custom class from another package.
1. '/' usually acts as a divider; points of reference include:
- path names in the terminal, where '/' separates directories
- writing, where '/' separates two words
- math, where '/' separates numerator and denominator
2. Based on our introduction to venvs in class, I predict that this will print
in the terminal, before the prompt, to let you know that you are in the venv.
3. It will print "(<venv name>)"
4. Prior to running app.py, it was not clear that "No hablo queso!" would appear
anywhere, because I don't know if run() calls hello_world().
It did appear, but not in the terminal! After the warning, the terminal printed
'Running on http://127.0.0.1:5000', and clicking on the link brought me to a website
which has "No hablo queso!"
5. In java, calling an object's method has the format <object>.<method>(<parameters>),
which is a similar construct.
 ...


INVESTIGATIVE APPROACH:
Based on the instructions received in class, we created a venv, installed flask
using pip, and successfully ran app.py, which ran a website.
'''




from flask import Flask


app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?


@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?


app.run()                                # Q5: Where have you seen similar constructs in other languages?
