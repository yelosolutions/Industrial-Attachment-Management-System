from flask import abort
from flask_login import current_user
from app import db, admin
from flask_admin.contrib.sqla import ModelView
from app.models import User, Application

class Control(ModelView):
    def is_accessible(self):
        if current_user.is_admin == True:
            return current_user.is_authenticated
        else:
            return abort(404)
    def not_auth(self):
        return "You need to be an admin in order to access the Admin Panel"

admin.add_view(Control(User, db.session))
admin.add_view(Control(Application, db.session))
