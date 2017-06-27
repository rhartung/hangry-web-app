"""Server holds routes for Flask app."""

from flask import Flask, jsonify, render_template
from flask import redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from data_model import connect_to_db, db, User, Cuisine


app = Flask(__name__)

app.secret_key = ""  # need to create secret key & fill this in


@app.route("/")
def homepage():
    """Homepage shows user login or acct creation link."""

    return render_template("homepage.html")


@app.route("/create-account")
def show_acct_form():
    """Display form to create Hangry account."""

    return render_template("create-account.html")


@app.route("/create-account", methods=["POST"])
def create_acct():
    """Sends user's account creation form to database."""

    pass


@app.route("/profile")  # will need route to go to specific user page
def show_user():
    """Shows user's profile page."""

    pass


@app.route("/search")
def search():
    """Display search form - search by cuisine or restaurant name."""

    pass


@app.route("/search-results")  # need route to show results specific to search
def show_results():
    """Show results of user's search - factor in user location."""

    pass


@app.route("/login", methods=["POST"])
def log_user_in():
    """Logs user into account based on form input."""

    pass


if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)  # need secret key for this to work

    app.run(port=5000, host="0.0.0.0")
