from flask import Flask, render_template

#Flask can create website objects

app = Flask("Website")

# when a user browses like:  <website-url>/home, myhome function will return then html page
# so, put html file into a dir named: "templates"
# http://127.0.0.1:5000/home

@app.route("/home")
def myhome():
    return render_template("tutorial.html")

@app.route("/about/")
def about():
    return render_template("about.html")

app.run(debug=True)

