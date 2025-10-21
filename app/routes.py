from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            x = float(request.form["x"])
            y = float(request.form["y"])
            op = request.form["operation"]
            if op == "add":
                result = x + y
            elif op == "subtract":
                result = x - y
            elif op == "multiply":
                result = x * y
            elif op == "divide":
                result = "Cannot divide by zero" if y == 0 else x / y
        except Exception:
            result = "Invalid input"
    return render_template("index.html", result=result)
