from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/try')
def trye():
    return render_template("canvatry.html")

@app.route('/new')
def tryei():
    return render_template("brushing-canvas.html")


@app.route('/reward')
def reward():
    return render_template("reward.html")

@app.route("/data")
def data():
    l=""
    with open("/home/theo/PycharmProjects/rufus/log_2.csv","r") as f:
        for line in f:
            l+=line
    return l



if __name__ == '__main__':
    app.run()
