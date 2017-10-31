from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)

@app.route("/")

def gettime():
	localtime = datetime.datetime.now()
	strTime = localtime.strftime("%Y-%m-%d %H:%M")

	templateData = {
		'title' : 'LocalTime',
		'time' : strTime
	}
	return render_template('main.html', **templateData)


if __name__ == "__main__":
        app.run(host='192.168.0.13', port=8888, debug=True)
