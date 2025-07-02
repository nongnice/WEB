import os

from flask import Flask,render_template,request

app=Flask(__name__)

#app.config["TEMPLATES_AUTO_RELOAD"]=True

#db=SQL("sqlite://birthday.db")

#@app.after_request
#"""ENSURE REPONSE AREN'T CACHED"""
    #response.headers["Cache-Control"]="no-cache,no-store,must-revalidate"
    #response.headers["Expires"]=0
    #response.headers["pragma"]="no-cache"
    #return response
@app.route("/")
def index():
       # html=render_template("index.html")
   # if request.method=="POST"
        #return redirect("/")
    #else:
        #return render_template("index.HTML")
        if "name" in request.args:
            name=request.args["name"]
        else:
              name="world"
        return render_template("index.html",placeholder=name)