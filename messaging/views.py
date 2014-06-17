# coding: utf-8
from flask import render_template, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required

from . import app, login_manager
from .forms import LoginForm
from .models import user_list


@login_manager.user_loader
def lookup_user(user_id):
    for user in user_list:
        if user.pk == user_id:
            return user


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        for user in user_list:
            # Authentication process was simplified intentionally.
            if user.name == form.name.data and user.password == form.password.data:
                login_user(user)
                return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
@login_required
def index():
    return 'hello world'
