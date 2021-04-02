from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
<!DOCTYPE html>
<head>
   <title>Employees</title>
</head>
<center> 
<body style="width: 880px; margin: auto; background-color:powderblue;"> 
    <h1>Hello Employees !!!</h1>
    <p>Good Morning :)</p>
    <img src="https://blog.clickdimensions.com/wp-content/uploads/2017/04/BlogFeatureImage-NewEmployees.png" alt="Welcome">
    <img src="https://media1.giphy.com/media/xTiTnl2gE4jRamfPnW/giphy.gif" alt="let's party">
</body>
</center> 
</style>
"""

@app.route("/hi/")
def who():
    return "how are you? what are you doing?"

@app.route("/hi/<username>")
def great(username):
    return f"Hello {username}!!"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)
