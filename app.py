from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

infor = []

@app.route("/")
def home():
    return render_template("index.html", infor=infor)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    message = request.form.get("message")
    for n, m in infor:
        if n == name and m == message:
            return redirect(url_for("home"))
    infor.append([name, message])
    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(infor):
        infor.pop(index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
