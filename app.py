from flask import Flask,render_template
app = Flask(__name__)

@app.route("/View")
def View():
    return render_template("home.html")


@app.route("/api")
def hello():
    return "Hello, World! Deployement in process"

if __name__ == "__main__":
    app.run()