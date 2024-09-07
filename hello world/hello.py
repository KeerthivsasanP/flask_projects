from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello world"
@app.route("/greet/<username>")
def greet(username):
    return f"<h1>Hello {username}<h1>"

if __name__ == "__main__":
    app.run(debug=True)