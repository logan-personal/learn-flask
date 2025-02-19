# Flask Demo Project

# 1. Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import pyodbc


# 2. Creating a Flask app instance
# This creates an instance of the Flask class, which is the WSGI application.
# __name__ is a special Python variable that gets the name of the current module.
# It's used by Flask to determine the root path of the application.
app = Flask(__name__)


# 3. Defining a basic route
# The @app.route decorator is used to bind a function to a URL.
# When a user visits the specified URL, the decorated function will be executed.
# In this case, the '/' route is bound to the hello_world function.
@app.route("/")
def hello_world():
    """
    This function is executed when the user visits the root URL ('/').
    It returns a simple string "Hello, World!" to the browser.
    """
    return "Hello, World!"


# Example route with variable
@app.route("/user/<username>")
def show_user_profile(username):
    """
    This function demonstrates how to use variable parts in a URL.
    The <username> part of the URL is a variable that will be passed to the function.
    """
    return f"User: {username}"


# Example route with HTML rendering
@app.route("/template")
def render_template_example():
    """
    This function demonstrates how to render an HTML template.
    It uses the render_template function to load and render the 'index.html' template.
    """
    return render_template("index.html", message="Hello from Flask!")


# Example route with form handling
@app.route("/form", methods=["GET", "POST"])
def handle_form():
    """
    This function demonstrates how to handle a form submission.
    It uses the request object to access the form data.
    """
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("form.html")


# Example route with redirection
@app.route("/redirect")
def do_redirect():
    """
    This function demonstrates how to redirect to another route.
    It uses the redirect function to redirect to the 'hello_world' route.
    """
    return redirect(url_for("hello_world"))


# 4. Running the app in debug mode
# The app.run() method starts the Flask development server.
# Setting debug=True enables debug mode, which provides helpful error messages
# and automatically reloads the server when you make changes to the code.
if __name__ == "__main__":
    app.run(debug=True)
