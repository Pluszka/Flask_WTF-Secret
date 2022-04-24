from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

class LoginF(FlaskForm):
    login = StringField(label='Login', validators=[DataRequired(), Email()])
    passw = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')

app.config['SECRET_KEY'] = 'any secret string'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    log_form = LoginF()
    if log_form.validate_on_submit():
        if log_form.login.data == 'admin@email.com' and log_form.passw.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=log_form)

@app.route('/success', methods=['POST', 'GET'])
def success():
    return render_template('success.html')

@app.route('/den', methods=['POST', 'GET'])
def den():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)