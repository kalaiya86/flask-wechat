from app import app
# from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Required
from flask import Flask, render_template, session, redirect, url_for

class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')



@app.route('/index')
def index():
    return render_template('login.html', form=form, name=name, class_body='login-body')

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    name = None
    form = LoginForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', 
        form=form, 
        name=name, 
        class_body='login-body',
        providers = app.config['OPENID_PROVIDERS']
        )