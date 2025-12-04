from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "game123"

@app.route("/")
def index():
    return render_template("index.html")

# 1. Тоо таах
@app.route("/guess")
def guess():
    session["num"] = random.randint(1, 100)
    return render_template("guess.html")

@app.route("/api/guess", methods=["POST"])
def api_guess():
    num = session.get("num")
    g = int(request.json["guess"])
    if g == num:
        return jsonify(msg="🎉 ЗӨВ!")
    elif g < num:
        return jsonify(msg="🔼 Их байна")
    else:
        return jsonify(msg="🔽 Бага байна")

# 2. Хайч Чулуу Даавуу
@app.route("/rps")
def rps():
    return render_template("rps.html")

@app.route("/api/rps", methods=["POST"])
def api_rps():
    user = request.json["choice"]
    ai = random.choice(["rock","paper","scissors"])
    if user == ai:
        result = "ТЭНЦЛЭЭ"
    elif (user=="rock" and ai=="scissors") or (user=="paper" and ai=="rock") or (user=="scissors" and ai=="paper"):
        result = "ЧИ ХОЖЛОО ✅"
    else:
        result = "ЧИ ХОЖИГДЛОО ❌"
    return jsonify(ai=ai, result=result)

# 3. Зураг таах
@app.route("/image")
def image():
    return render_template("image_guess.html")

# 4. Фибоначчи
@app.route("/fibonacci", methods=["GET","POST"])
def fibonacci():
    result = None
    if request.method == "POST":
        n = int(request.form["n"])
        fib = [0,1]
        for i in range(2,n):
            fib.append(fib[-1]+fib[-2])
        result = fib
    return render_template("fibonacci.html", result=result)

# 5. Төөрдөг байшин (Demo)
@app.route("/maze")
def maze():
    return render_template("maze.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

