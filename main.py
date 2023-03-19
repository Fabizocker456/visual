import flask
app = flask.Flask("__main__")
import all_blocks

import base_blocks as _

@app.route("/")
def index():
    return flask.Response(flask.render_template("index.html"), mimetype="text/html")

@app.route("/style.css")
def style():
    return flask.Response(flask.render_template("style.css"), mimetype="text/css")

@app.route("/main.js")
def script():
    return flask.Response(flask.render_template("main.js"), mimetype="text/javascript")

@app.route("/gen.js")
def gen():
    return flask.Response(flask.render_template("gen.js", blocks=all_blocks.gen()), mimetype="text/javascript")

app.run("0.0.0.0", 8080, True)
