from flask import Flask, render_template, flash, url_for, session, redirect, request, logging
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

class RegisterForm(Form):
    name = StringField('Name', [validators.length(min=4,max=50)])
    username = StringField('Username',[validators.length(min=4, max=25)])
    email = StringField('Email', [validators.length(min=6,max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm','Password didn\'t match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')

#if __name__=='__main__':
    #app.run(debug=True)