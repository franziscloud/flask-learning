from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators= [
        DataRequired(),
        Length(min=2, max=50)
    ])
    
    email = StringField('Email', validators = [
        DataRequired(),
        Email()
    ])
    
    message = TextAreaField('Message', validators = [
        DataRequired(),
        Length(min=10, message='Message must be at least 10 characters')
    ])
    
    submit = SubmitField('Send Message')