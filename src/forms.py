from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SearchForm(FlaskForm):
    item = StringField('Item Search', validators=[DataRequired()])
    min_price = FloatField('Minimum Price')
    max_price = FloatField('Maximum Price')
    submit = SubmitField('Search')
