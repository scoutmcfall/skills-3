from flask import Flask, redirect, request, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "DEV"

# The top melons at Ubermleon
MOST_LOVED_MELONS = {
    "cren": {
        "img": "http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg",
        "name": "Crenshaw",
        "num_loves": 584,
    },
    "jubi": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg",
        "name": "Jubilee Watermelon",
        "num_loves": 601,
    },
    "sugb": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg",
        "name": "Sugar Baby Watermelon",
        "num_loves": 587,
    },
    "texb": {
        "img": "http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg",
        "name": "Texas Golden Watermelon",
        "num_loves": 598,
    },
}


# TODO: replace this comment with your code
@app.route("/")
def index():
    """Return homepage.Do I already have something called username in my cookies
    If not, submit name via form, then send me to top melons"""
    if "username" in session:
        return redirect("/top-melons")
        
    return render_template("homepage.html")

@app.route("/get-name")
def get_name():
    username = request.args.get("name", "")#use form in homepage and put info in args
    session["username"] = username
    return redirect("/top-melons")

@app.route("/top-melons")
def top_melons():
    """Return page showing the most loved melons"""
    username = request.args.get("name")
    if username in session:
        return render_template("top-melons.html", melon_dict = MOST_LOVED_MELONS, name = "username")
    else:
        return redirect("/")
    

@app.route("/love-melon", methods=["POST"])
def love_melon():
    melon = request.form.get("melon")
    session[melon]+= 1
    return render_template("thank-you.html", name = "username")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
