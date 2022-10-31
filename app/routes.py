from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RequestForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Joseph Rono'}
    req_posts = [
        {
            'student': {'username': 'Joel'},
            'body': 'I need an attachment in KCB bank'
        },
        {
            'student': {'username': 'Soi'},
            'body': 'I need an attachment in Kenyatta University'
        }
    ]
    remark_posts = [
        {
            'lecturer': {'username': 'Mwangi'},
            'body': 'Joel did a great work, He deserves an A'
        }
    ]
    return render_template('index.html', title='Home', user=user, req_posts=req_posts, remark_posts=remark_posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Validation required for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('login.html', title="Sign In", form=form)

@app.route('/request', methods=['GET', 'POST'])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        flash('Validation required for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('request.html', title="Request", form=form)