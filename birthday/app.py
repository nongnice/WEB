from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/" ,methods=["GET","POST"])
def index():
    if request.method == "POST":
        name_input = request.form.get("name","world")
        return render_template("greet.html",name=name_input)
    else:
        return render_template("index.html")