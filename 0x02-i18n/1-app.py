#!/usr/bin/env python3
"""
Basic Babel setup
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    return: index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)
