from flask import Flask
# the class Flask has a CAPITAL F - MUST REMEMBER THAT OTHERWISE WILL PRODUCE ERROR

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my first site"

@app.route('/apples/')
def applessite():
    return "There are no apples here"


if __name__ == "__main__":
    app.run(debug=True)
