import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/try')
def trye():
    return render_template("canvatry.html")


@app.route('/new/<foo>')
def tryei(foo):
    return render_template("brushing-canvas.html")


@app.route('/reward')
def reward():
    return render_template("reward.html")

@app.route('/deepviz')
def dv():
    return render_template("deepviz.html")


@app.route("/data/<dataset>")
def data(dataset):
    l = ""
    with open("logs/"+dataset, "r") as f:
        for line in f:
            l += line
    return l


@app.route("/up", methods=['POST'])
def up():
    file = request.files['file']
    file.save(os.path.join(os.getcwd() + "/logs", file.filename))
    return "ok"


@app.route("/getnames", methods=['GET'])
def getnames():
    mes =""

    for f in getfile(os.getcwd() + "/logs"):
        mes+=f+","
    mes = mes[:-1]
    return mes


def getfile(path):
    files = []
    file = [".csv"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]  # reverse search of '.' and send it. If no '.', send empty String
        if ext.lower() not in file:
            continue
        files.append(f)

    return files


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
