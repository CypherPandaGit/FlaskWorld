from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextField, TextAreaField,
                     SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'


class InfoForm(FlaskForm):

    breed = StringField('What breed are you?', validators=[])
