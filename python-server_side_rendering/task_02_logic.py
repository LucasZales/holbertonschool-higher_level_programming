#!/usr/bin/python3
"""
Flask app with a page that shows items from a JSON file
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def home():
    """Home page"""
    return render_template("index.html")


@app.route("/about")
def about():
    """About page"""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Contact page"""
    return render_template("contact.html")


@app.route("/items")
def items():
    """Show items from JSON"""

    with open("items.json", "r") as file:
        data = json.load(file)

    items = data.get("items", [])
    return render_template("items.html", items=items)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
