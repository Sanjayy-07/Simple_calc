from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(force=True)
    op = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid number input"}), 400

    try:
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                return jsonify({"error": "Division by zero"}), 400
            result = a / b
        elif op == "%":
            result = a % b
        elif op == "^":
            result = a ** b
        else:
            return jsonify({"error": "Unsupported operation"}), 400

        # Return a float or an int-friendly value
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)