# peaches & mangoes: Anastasia, Nia, Naomi
# SoftDev
# Oct 2024

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()