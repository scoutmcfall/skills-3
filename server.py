from flask import Flask, redirect, request, render_template, session
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
    """Return homepage."""

    return render_template("homepage.html")

@app.route("/top-melons")
def top_melons():
    """Return page showing the most loved melons"""

    return render_template("top-melons.html",
                           most_loved_melons = MOST_LOVED_MELONS)

@app.route("/login", methods=["POST"])
def process_login():
    """Collect user name

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """
    session[name] = name
    flash ("we got your name!")
   
    name = request.form.get("name")
    session[name] = name
    flash ("we got your name!")
    name_list = []
    return redirect("/top-melons")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
