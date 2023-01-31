from flask import Flask, render_template, request, flash

# Creates a class for the app
app = Flask(__name__, template_folder = "template")

app.secret_key = "12345"

@app.route("/")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input'] + ", greetings!"))
    return render_template("index.html")

if __name__=="__main__":
    app.run()