#!/usr/bin/env python3
"""
Basic Babel setup
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ['en', 'fr']
