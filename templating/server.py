from flask import Flask,render_template
app = Flask(__name__)

@app.route("/<username>")
def printHello(username):
    return render_template("index.html",name=username)



if __name__ == "__main__":
    app.run(debug=True)