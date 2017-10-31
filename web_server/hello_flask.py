from  flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return("hello raspberryp with flask!")

if __name__ == "__main__":
	app.run(host='192.168.0.13', port=8888, debug=True)

