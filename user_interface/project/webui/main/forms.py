from email.policy import default
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField

class AddStartStopForm(FlaskForm):
    start_time_min =  FloatField('Start time (min)', default=0)
    add_time = SubmitField('Add time set')