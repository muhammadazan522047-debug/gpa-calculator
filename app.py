from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    gpa = None
    percentage = None
    if request.method == "POST":
        try:
            marks = [
                int(request.form["sub1"]),
                int(request.form["sub2"]),
                int(request.form["sub3"]),
                int(request.form["sub4"]),
                int(request.form["sub5"]),
                int(request.form["sub6"]),
                int(request.form["sub7"])
            ]
            total = sum(marks)
            percentage = (total / 700) * 100

            gpa_scale = {
                85: 4.0, 84: 3.9, 83: 3.8, 82: 3.7, 81: 3.6, 80: 3.5,
                79: 3.4, 78: 3.4, 77: 3.3, 76: 3.3, 75: 3.2, 74: 3.2,
                73: 3.1, 72: 3.0, 71: 2.9, 70: 2.8, 69: 2.7, 68: 2.6,
                67: 2.5, 66: 2.5, 65: 2.4, 64: 2.4, 63: 2.3, 62: 2.2,
                61: 2.1, 60: 2.0, 59: 1.9, 58: 1.8, 57: 1.7, 56: 1.6,
                55: 1.5, 54: 1.4, 53: 1.3, 52: 1.2, 51: 1.1, 50: 1.0
            }

            if percentage >= 85:
                gpa = 4.0
            elif percentage < 50:
                gpa = 0.0
            else:
                gpa = gpa_scale.get(int(percentage), "No exact match")
        except:
            gpa = "Invalid Input"

    return render_template("index.html", gpa=gpa, percentage=percentage)

if __name__ == "__main__":
    app.run(debug=True)
