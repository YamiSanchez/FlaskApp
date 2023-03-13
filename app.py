from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
     if request.method == "POST":
        if request.form["contraseña"].isalnum() == True:
           return redirect(url_for("success"))
        return redirect(url_for("login"))
     return render_template("login.html")


@app.route("/success")
def success():
  return render_template("success.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=5000)