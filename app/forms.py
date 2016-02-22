from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class InputForm(Form):
    input = StringField('input', validators = [DataRequired()])
