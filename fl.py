from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def mp3():
	return None


if __name__ == '__main__':
    app.run(debug=True)
