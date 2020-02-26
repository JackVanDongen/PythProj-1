from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Here is the latest webserver!"

@app.route("/info")
def info():
	return "This the response to the info page request"

if __name__ == "__main__": 
	app.run(host="0.0.0.0", port=80, debug=True)
