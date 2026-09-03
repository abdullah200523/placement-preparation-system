from flask import Flask, render_template, request

app = Flask(__name__)


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("home.html")


# ---------------- LOGIN PAGE ----------------

@app.route("/login")
def login():
    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard", methods=["POST"])
def dashboard():

    name = request.form["name"]

    return render_template(
        "dashboard.html",
        name=name
    )


# ---------------- QUIZ PAGE ----------------

@app.route("/quiz")
def quiz():

    return render_template("quiz.html")


# ---------------- QUIZ RESULT ----------------

@app.route("/result", methods=["POST"])
def result():

    score = 0

    if request.form.get("q1") == "30":
        score += 1

    if request.form.get("q2") == "25":
        score += 1

    if request.form.get("q3") == "Python":
        score += 1

    if request.form.get("q4") == "10":
        score += 1

    if request.form.get("q5") == "15":
        score += 1

    if request.form.get("q6") == "30":
        score += 1

    if request.form.get("q7") == "10":
        score += 1

    if request.form.get("q8") == "7":
        score += 1

    if request.form.get("q9") == "25":
        score += 1

    if request.form.get("q10") == "25":
        score += 1

    percentage = (score / 10) * 100

    return f"""
    <div style="text-align:center; margin-top:100px;">

        <h1>Quiz Completed 🎉</h1>

        <h2>Your Score: {score}/10</h2>

        <h2>Percentage: {percentage}%</h2>

        <br>

        <a href="/quiz">Try Again</a>

        <br><br>

        <a href="/login">Go Home</a>

    </div>
    """
    return f"""
    <!DOCTYPE html>

    <html>

    <head>
        <title>Quiz Result</title>

        <style>

            body {{
                font-family: Arial;
                background-color: #f2f6ff;
                text-align: center;
                margin-top: 100px;
            }}

            .result {{
                background: white;
                width: 400px;
                margin: auto;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 10px #ccc;
            }}

            h1 {{
                color: #1769aa;
            }}

            h2 {{
                color: #333;
            }}

            a {{
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                background-color: #1769aa;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}

        </style>

    </head>

    <body>

        <div class="result">

            <h1>Quiz Completed 🎉</h1>

            <h2>Your Score: {score}/3</h2>

            <a href="/quiz">Try Again</a>

            <a href="/login">Go Home</a>

        </div>

    </body>

    </html>
    """


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)