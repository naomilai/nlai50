# Naomi, Kishi, ?
#   Hungry
#   Oct 8 2024

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    # print("***DIAG: request.args ***")
    # print(request.args)
    # # print("***DIAG: request.args['username']  ***")
    # # print(request.args['username'])
    # print("***DIAG: request.headers ***")
    # print(request.headers)
    # print("***DIAG: request.method ***")
    # print(request.method)
    # print("***DIAG: request.form ***")
    # print(request.form)
    return render_template( 'login.html' )


@app.route("/auth" , methods=['GET', 'POST'])
def authenticate():
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    # print("***DIAG: request.args ***")
    # print(request.args)
    # print("***DIAG: request.args['username']  ***")
    # # print(request.args['username'])
    # # print("***DIAG: request.headers ***")
    # print(request.headers)
    # print("***DIAG: request.method ***")
    # print(request.method)
    # print("***DIAG: request.form ***")
    # print(request.form)

    re = "re"
    if(request.method == "GET"):
         re = request.args['username']
    else:
        re = request.form['username']
    # print(re)

    return render_template( 'response.html', 
        info = re,
        method=request.method)  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
