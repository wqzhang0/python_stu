from wtforms import Form, validators, TextField, PasswordField, BooleanField


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=3, max=25)])
    email = TextField('Email Address', [validators.Length(min=3, max=25)])
    password = PasswordField('New Password',
                             [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    accept_rules = BooleanField('I accept the site rules', [validators.Required()])