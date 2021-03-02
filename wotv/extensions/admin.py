from flask_admin import Admin
"""from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
"""
from flask_simplelogin import login_required

def verifylogin(user):
    return user.get("username")=="admin" and user.get("password")=="123456"
