import os
from datetime import timedelta

import binascii
from flask import Flask, render_template, request, session, redirect
from flask_caching import Cache
from flask_compress import Compress

app = Flask(__name__)

app.secret_key = binascii.hexlify(os.urandom(24))

# GZIP
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/csv', 'text/xml', 'application/json', 'application/javascript']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)
Compress(app)


@app.before_request
def make_session_permanent():
    session.permanent = False
    app.permanent_session_lifetime = timedelta(minutes=10)
    if session.get("dataset") is None:
        temp = getfile(os.getcwd() + "/logs")
        temp.sort()
        session["dataset"] = temp[len(temp) - 1]


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/try')
def trye():
    return render_template("canvatry.html")


@app.route('/new')
def tryei():
    return render_template("brushing-canvas.html")


@app.route('/reward')
def reward():
    return render_template("reward.html")


@app.route('/deepviz')
def dv():
    return render_template("deepviz.html")


@app.route('/traj')
def dvo():
    return render_template("ranking-grid.html")


@app.route("/data/<dataset>")
def data(dataset):
    l = ""
    with open("logs/" + dataset, "r") as f:
        for line in f:
            l += line
    return l


@app.route("/up", methods=['POST'])
def up():
    file = request.files['file']
    file.save(os.path.join(os.getcwd() + "/logs", file.filename))
    return "ok"


@app.route("/select/<dataset>", methods=['GET'])
def selec(dataset):
    session["dataset"] = dataset
    return redirect("/new")


@app.route("/name", methods=['GET'])
def nam():
    return session["dataset"]


@app.route("/getnames", methods=['GET'])
def getnames():
    mes = ""
    temp = getfile(os.getcwd() + "/logs")
    temp.sort()
    for f in temp:
        mes += f + ","
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
