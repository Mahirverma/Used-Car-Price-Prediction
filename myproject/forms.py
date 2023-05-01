# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Email, EqualTo
# from wtforms import ValidationError
# from myproject.models import User

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Sign In')

# class RegistrationForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(),Email()])
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
#     pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
#     submit = SubmitField('Sign Up')

#     def validate_email(self, email):
#         if User.query.filter_by(self.email.data==email).first():
#             raise ValidationError('Email has been registered!')
#     def validate_username(self, username):
#         if User.query.filter_by(self.username.data==username).first():
#             raise ValidationError('Username has been registered!')
