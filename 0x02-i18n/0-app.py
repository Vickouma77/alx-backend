#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    return index page
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
