from flask import Flask
app = Flask(__name__)


@app.route("/info")
def lwinfo():
	return " I am lw"

@app.route("/phone")
def lwphonw():
	return "9274881980"

app.run(host="0.0.0.0")