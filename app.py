from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return(render_template("index.html"))


@app.route("/main",methods=["GET","POST"])
def main():
   = request.fore.get("name")
  return(render_template("main.html",r=name))

@app.route("/imageGPT",methods=["GET","POST"])
def main():
  return(render_template("imageGPT.html",r=name))

if __name__ == "__main__":
  app.run()
