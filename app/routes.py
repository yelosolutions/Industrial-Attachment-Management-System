from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User
from app.forms import LoginForm, RequestForm, StudentForm, NamerForm, RegistrationForm
from flask import request
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title="Sign In", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You are now registered!")
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route('/add', methods=['GET', 'POST'])
@login_required
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
@login_required
def request_att():
    form = RequestForm()
    if form.validate_on_submit():
        flash('Request Form Submitted for {} '.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('request_att.html', title="Request", form=form)

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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))