from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = ' dhuiqwhfudeiwf fewjfhiewf'

from routes import views

