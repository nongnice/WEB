import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

conn=sqlite3.connect('frosh.db', check_same_thread=False)


SPORTS = [
       "Basketball",
       "Soccer",
       "Ultimate frisbee",
]



@app.route("/")

def index():
        return render_template("index.html",sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
        cursor=conn.cursor()
        name=request.form.get("Name")
        if not name:
                return render_template("error.html", message="missing name")
        
        sport=request.form.get("sport")
        if not sport:
                return render_template("error.html", message="missing sport")
        if sport not in SPORTS:
                return render_template("error.html", message="Invalid sport")
        
        cursor.execute("INSERT INTO registrants (sport, name) VALUES(?, ?)", (sport, name))
        conn.commit()
        return render_template("success.html")
@app.route("/registrants")
def registrants():
        cursor=conn.cursor()
        ret=cursor.execute("select name, sport from registrants")
        registrants=ret.fetchall()
        
        return render_template("registrants.html", registrants=registrants)