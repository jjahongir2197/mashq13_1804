from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def grade():

    if request.method == "POST":

        score = int(request.form["score"])

        if score >= 90:
            grade = "A"

        elif score >= 80:
            grade = "B"

        elif score >= 70:
            grade = "C"

        elif score >= 60:
            grade = "D"

        else:
            grade = "F"

        return f"Sizning bahoyingiz: {grade}"

    return render_template("index.html")

app.run(debug=True)
