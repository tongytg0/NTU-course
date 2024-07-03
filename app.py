#import lib
from flask import Flask, render_template, request

#api google
import google.generativeai as palm
palm.configure(api_key="AIzaSyBF-fXqYk5VLQ6E7UIuiViLxQ-B9wScdPI")
model = {"model": "models/chat-bison-001"}

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
    r = request.form.get("q")
    print(r)
    return(render_template("main.html",r=r))

@app.route("/traffic_thailand", methods=["GET","POST"])
def traffic_thailand():
    q = "thailand traffic"
    r = palm.chat(**model, messages=q)
    return(render_template("traffic_thailand.html",r=r.last))

@app.route("/traffic_singapore", methods=["GET","POST"])
def traffic_singapore():
    q = "singaoore traffic"
    r = palm.chat(**model, messages=q)
    return(render_template("traffic_singapore.html",r=r.last))

if __name__ == "__main__":
    app.run()
