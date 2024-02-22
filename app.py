from flask import Flask,request,render_template
import replicate
import os
import time
from openai import OpenAI

openai_api_key=os.getenv("OPENAI_API_KEY")
os.environ["REPLICATE_API_TOKEN"]="r8_ce57ooEmWgSqmS6BqjCBGSWW2waTZTg3N2bhg"

model = OpenAI(api_key=openai_api_key)

app = Flask(__name__)

r = ""
first_time = 1

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("remarks.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global r,first_time
    if first_time==1:
        r = request.form.get("r")
        first_time=0
    return(render_template("main.html",r=r))

@app.route("/text_gpt",methods=["GET","POST"])
def text_gpt():
    return(render_template("text_gpt.html"))

@app.route("/text_result",methods=["GET","POST"])
def text_result():
    q = request.form.get("q")
    r = model.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {
            "role" : "user",
            "content" : q
            }
        ]
    )
    time.sleep(5)
    return(render_template("text_result.html",r=r.choices[0].message.content))

@app.route("/text_gpt",methods=["GET","POST"])
def text_gpt():
    return(render_template("text_gpt.html"))

@app.route("/text_result",methods=["GET","POST"])
def text_result():
    q = request.form.get("q")
    r = model.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {
            "role" : "user",
            "content" : q
            }
        ]
    )
    time.sleep(5)
    return(render_template("text_result.html",r=r.choices[0].message.content))



@app.route("/end",methods=["GET","POST"])
def end():
    global first_time,r
    first_time = 1
    return(render_template("end.html",r=r))

if __name__ == "__main__":
    app.run()
