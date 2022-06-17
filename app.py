from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    return "This is my first machine larning flask app"

if __name__ == "__main__":
    app.run(debug = True)