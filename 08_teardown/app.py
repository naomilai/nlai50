# Naomi Lai
# Belugas
# SoftDev
# K08 -- Flask
# 2024-09-20
# time spent: 1.5

'''
DISCO:
<note any discoveries you made here... no matter how small!>
Some modules are not part of the standard library
pip = "pip installs python": command for downloading more packages from terminal
"$pip install flask": will fail at start or during install bc of machine
run "$python3 -m venv foo"
can do "l;" or maybe "ls-al" to see foo folder
cd into it and see that it has a virtual python environment
to activate go to home dir and "usrname@cslab3-24:~$ . path/to/foo/bin/activate"
success = (foo) before usrname
run "deactivate" when wanted
now you can use virtual machine wherever you are

QCC:
0. This syntax kind of reminded me of Java, especially when you open a file and you do something like "File x = new File(fileName.extension)"
1. The major point of reference for '/' is in terminal and it is used for direectory, particularly the root directory
2. This will print in the terminal when you visit the link.
3. It will print "__main__"
4. It will appear in the http link that is provided in the terminal. I kind of accidentally stumbled upon it, but also you can kind of assume that the route command is used to route the output elsewhere, which is why I clicked the link.
5. This simply reminds me of java calling a function.
 ...
 Why does the "print(__name__)" print after quitting the function? Update: On school lab computers, it prints when link is visited.
 So what exactly does .route establish? Is a temporary file setup somewhere, because I could not find any in the total root directory or in the folder it was in?


INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 I first tried my best to read through the code as best I could, to find any similarities with things I may have
 seen in the past, and roughly understand the idea of what I am looking at. After running the code in the terminal
 several times, to observe behavior, I investigated the link. After I got all I thought I could get from the
 immediate info in front of me, I looked up Flask documentation, so I could get an actual description of the
 individual functions.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs? Java? the returns are similar, but print is not.

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'? entering a new/different directory?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print? It will print 'No hablo queso' to a page, shown as a link.
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know? Yes-- when run in the terminal, a link a page is returned.

app.run()                                # Q5: Where have you seen similar constructs in other languages? Java? (app.run())