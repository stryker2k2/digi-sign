from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "DIGI-SIGN"


# User Login Form Class
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Route Decorator
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    username = ''
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        form.username.data = ''
    return render_template('admin.html', form=form, username=username)