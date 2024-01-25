from flask import Flask
app = Flask(__name__)

@app.route("/api")
def hello():
    return "Hello, World! Deployement in process"

if __name__ == "__main__":
    app.run()