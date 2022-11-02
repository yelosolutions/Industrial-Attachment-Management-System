from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RequestForm, NamerForm, SignupForm

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', title='Home')

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Form Submited Successfully")
    return render_template('login.html', title="Sign In", form=form)

@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash("Form Submited Successfully")
    return render_template('signup.html', title="Sign Up", form=form)

@app.route('/request', methods=['GET', 'POST'])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        flash('Request Form Submitted for {} '.format(
            form.username.data))
        return redirect(url_for('/index'))
    return render_template('request.html', title="Request", form=form)

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Form Submitted Successfully')
        #return redirect(url_for('/index'))
    return render_template('name.html', title="Name", name=name, form=form)