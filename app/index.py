from flask import Flask
app = Flask(__name__)

@app.route("/") 
def index():
	return ('<h1>hello. world staging 7</h1>')
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)