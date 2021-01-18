from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "welcome to index page"

@app.route("/hi/")
def who():
    return "Who are you?"

@app.route("/hi/<username>")
def great(username):
    return f"Hello {username}!!"

if __name__ == "__main__":
    app.run()