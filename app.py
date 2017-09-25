from flask import Flask
app= Flask(__name__)

@app.route("/rick")
def hello_world():
    return "WUBBA LUBBA DUB DUB"


@app.route("/morty")
def test2():
    return "Oh geez man"


@app.route("/noobnoob")
def test3():
    return "Woahh I'm nervous about my first mission!"

if __name__ == "__main__":
    app.debug = True
    app.run()
