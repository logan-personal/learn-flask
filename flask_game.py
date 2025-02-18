from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder="constructExport", template_folder="templates")


# Serve the HTML5 game from the "constructExport" directory
@app.route("/game")
def game():
    try:
        # List all files in the constructExport directory
        files = os.listdir("constructExport")
        # Find the main HTML file for the game (assuming it's named index.html)
        game_file = next((f for f in files if f.lower() == "index.html"), None)
        if game_file:
            # If index.html is in the root directory, use send_from_directory('.', game_file)
            return send_from_directory("constructExport", game_file)
        else:
            return "Error: index.html not found in constructExport directory", 404
    except FileNotFoundError:
        return "Error: constructExport directory not found", 404


# Serve the "introPage.html" from the "templates" directory
@app.route("/welcome")
def welcome():
    try:
        return render_template("introPage.html")
    except FileNotFoundError:
        return "Error: introPage.html not found in templates directory", 404


if __name__ == "__main__":
    # For production deployments, disable debug=True and consider using a production-ready web server.
    app.run(debug=True)
