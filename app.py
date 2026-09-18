from flask import Flask, render_template, request

app = Flask(__name__)


# =========================
# HOME
# =========================

@app.route("/")
def home():
    return render_template("home.html")


# =========================
# LOGIN
# =========================

@app.route("/login")
def login():
    return render_template("login.html")


# =========================
# DASHBOARD
# =========================

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    name = request.form.get("name", "Student")

    return render_template(
        "dashboard.html",
        name=name
    )


# =========================
# APTITUDE QUIZ
# =========================

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


# =========================
# QUIZ RESULT
# =========================

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
    <!DOCTYPE html>
    <html>
    <head>
        <title>Quiz Result</title>
    </head>

    <body>

        <div style="text-align:center; margin-top:100px;">

            <h1>🎉 Quiz Completed</h1>

            <h2>Your Score: {score}/10</h2>

            <h2>Percentage: {percentage}%</h2>

            <br>

            <a href="/quiz">
                <button>Try Again</button>
            </a>

            <a href="/dashboard">
                <button>Dashboard</button>
            </a>

        </div>

    </body>
    </html>
    """


# =========================
# EVEN OR ODD
# =========================

@app.route("/even-odd", methods=["GET", "POST"])
def even_odd():

    result = ""

    if request.method == "POST":

        number = int(request.form["number"])

        if number % 2 == 0:
            result = f"{number} is Even"
        else:
            result = f"{number} is Odd"

    return render_template(
        "even_odd.html",
        result=result
    )


# =========================
# PALINDROME
# =========================

@app.route("/palindrome", methods=["GET", "POST"])
def palindrome():

    result = ""

    if request.method == "POST":

        number = request.form["number"]

        if number == number[::-1]:
            result = f"{number} is a Palindrome"
        else:
            result = f"{number} is Not a Palindrome"

    return render_template(
        "palindrome.html",
        result=result
    )


# =========================
# SUM OF DIGITS
# =========================

@app.route("/sum-digits", methods=["GET", "POST"])
def sum_digits():

    result = ""

    if request.method == "POST":

        number = request.form["number"]

        total = 0

        for digit in number:
            total = total + int(digit)

        result = f"Sum of digits = {total}"

    return render_template(
        "sum_digits.html",
        result=result
    )


# =========================
# FACTORIAL
# =========================

@app.route("/factorial", methods=["GET", "POST"])
def factorial():

    result = ""

    if request.method == "POST":

        number = int(request.form["number"])

        fact = 1

        for i in range(1, number + 1):
            fact = fact * i

        result = f"Factorial of {number} = {fact}"

    return render_template(
        "factorial.html",
        result=result
    )


# =========================
# CODING PAGE
# =========================

@app.route("/coding")
def coding():
    return render_template("coding.html")


# =========================
# TECHNICAL INTERVIEW
# =========================

@app.route("/technical")
def technical():
    return render_template("technical.html")


# =========================
# HR INTERVIEW
# =========================

@app.route("/hr")
def hr():
    return render_template("hr.html")

@app.route("/resume", methods=["GET", "POST"])
def resume():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        location = request.form["location"]

        objective = request.form["objective"]

        education = request.form["education"]
        college = request.form["college"]
        year = request.form["year"]
        percentage = request.form["percentage"]

        skills = request.form["skills"]

        project = request.form["project"]
        project_description = request.form["project_description"]
        technologies = request.form["technologies"]

        internship = request.form.get("internship", "")
        internship_role = request.form.get("internship_role", "")
        internship_description = request.form.get(
            "internship_description", ""
        )

        certifications = request.form.get(
            "certifications", ""
        )

        languages = request.form.get(
            "languages", ""
        )

        linkedin = request.form.get(
            "linkedin", ""
        )

        github = request.form.get(
            "github", ""
        )

        return render_template(
            "resume_result.html",

            name=name,
            email=email,
            phone=phone,
            location=location,

            objective=objective,

            education=education,
            college=college,
            year=year,
            percentage=percentage,

            skills=skills,

            project=project,
            project_description=project_description,
            technologies=technologies,

            internship=internship,
            internship_role=internship_role,
            internship_description=internship_description,

            certifications=certifications,

            languages=languages,

            linkedin=linkedin,
            github=github
        )

    return render_template("resume.html")
# =========================
# RUN APPLICATION
# =========================
@app.route("/mock-result", methods=["POST"])
def mock_result():

    answers = {
        "q1": "50",
        "q2": "30",
        "q3": "HTML",
        "q4": "10",
        "q5": "25",
        "q6": "10",
        "q7": "7",
        "q8": "25",
        "q9": "25",
        "q10": "Python",
        "q11": "Database",
        "q12": "100",
        "q13": "#",
        "q14": "30",
        "q15": "MySQL",
        "q16": "81",
        "q17": "CSS",
        "q18": "60",
        "q19": "def",
        "q20": "20",
        "q21": "7/15",
        "q22": "9 1/5 days",
        "q23": "15 days",
        "q24": "22 1/2 days",
        "q25": "Rs. 400"
    }

    score = 0

    for question, correct_answer in answers.items():

        if request.form.get(question) == correct_answer:
            score += 1

    percentage = (score / 20) * 100

    return f"""
    <!DOCTYPE html>

    <html>

    <head>
        <title>Mock Test Result</title>
    </head>

    <body>

        <div style="text-align:center; margin-top:100px;">

            <h1>🎉 Mock Test Completed!</h1>

            <h2>Your Score: {score}/20</h2>

            <h2>Percentage: {percentage}%</h2>

            <br>

            <a href="/quiz">
                <button>🔄 Try Again</button>
            </a>

            <br><br>

            <a href="/dashboard">
                <button>🏠 Dashboard</button>
            </a>

        </div>

    </body>

    </html>
    """
if __name__ == "__main__":

    app.run(
        debug=True
    )