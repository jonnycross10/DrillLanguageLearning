from flask import Flask
from flask import send_file, render_template, request
from quizlet import quizletmp3

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route("/mp3", methods=['POST','GET'])
def mp3():
	text = request.form['text']
	print(text)
	quizletmp3(text)
	return send_file("text.mp3",as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
