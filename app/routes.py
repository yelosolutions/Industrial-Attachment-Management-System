from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import User
from app.forms import LoginForm, RequestForm, StudentForm, NamerForm, SignupForm

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

@app.route('/users/add', methods=['GET', 'POST'])
def add_student():
    name = None
    form = StudentForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(username=form.username.data, adm_number=form.adm_number.data, email=form.username.data)
            db.session.add(user)
            db.session.commit()
        name = form.username.data
        form.username.data = ''
        form.adm_number.data = ''
        form.email.data = ''
        flash("User Added Successfully")
    students = User.query.order_by(User.date_added)
    return render_template('add_student.html', title="Add",
        form=form,
        name=name,
        students=students)

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