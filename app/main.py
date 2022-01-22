from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html", currencies = ["c1", "c2"])
 # return "<h1>Homepage!</h1>"
  
  
@app.route("/about")
def about():
  return render_template("base.html")
  
  
if __name__ == "__main__":
  app.run(debug=True)

