


from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap

import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
  return render_template('500.html')

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['GET'])
def hello():
    # raise(Exception('500 error'))
    # mar = 'mar'[4]
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = session.get('username')
    # login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'username': username,
        'todos': todos
    }

    # if login_form.validate_on_submit():
    #     username = login_form.username.data
    #     session['username'] = username

    #     flash('Nombre de usuario registrado con éxito!')
    #     return redirect(url_for('index'))

    return render_template('hello.html', **context)