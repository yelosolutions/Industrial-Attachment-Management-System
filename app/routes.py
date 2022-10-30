from flask import render_template
from app import app

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