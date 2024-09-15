from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS=[
    {
        "id":1,
        "location": "Chennai",
        "salary": "Rs.1000000",
        "position": "Python developer"
    },
    {
        "id":2,
        "location": "Coimbatur",
        "salary": "Rs.800000",
        "position": "React developer",
    },
    {
        "id":3,
        "location": "Bengaluru",
        "salary": "Rs.600000",
        "position": "Oracle developer",
    }
]

@app.route("/")
def home():
    return render_template("index.html",jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)