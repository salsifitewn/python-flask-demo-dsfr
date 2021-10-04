from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)
from market import routes
