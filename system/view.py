from flask import (request, render_template, session, send_from_directory, make_response, redirect, url_for)
from system import app
from system.views import user

@app.route('/index')
@user.authorize
def index():
    user_list = session.get('user', None)
    username = user_list[0]["username"]
    return render_template("util/index.html", message='Hello, %s' % username)