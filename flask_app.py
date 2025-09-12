from flask import Flask, render_template, url_for, flash, session, redirect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Flaskform
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET KEY'] = 'Chave forte'
bootstrap = Bootstrap(app)
moment = Moment(app)

class Nameform(FlaskForm):
    name = StringField('What is your name?', validators = [DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validade_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.date:
            flash('Looks like you have changed your name!')
            session['name'] = form.name.data
            return redirect(url_for('index'))
    return render_template('index.html', form = form, name= session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', nome=name)

@app.route('/user/')
def userr():
    return render_template('user.html')

@app.route('/rotainexistente')
def rotainexistente(e):
    return render_template('404.html'), 404

@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome, prontuario, instituicao):
    return render_template('user.html', nome=nome, prontuario=prontuario, instituicao=instituicao)

from flask import request
@app.route('/contextorequisicao/<nome>')
def contextorequisicao(nome):
    requisicao = request.headers.get('User-Agent')
    IP = request.remote_addr
    host = request.host
    return render_template('contextorequisicao.html', nome=nome, requisicao=requisicao, IP=IP, host=host)

@app.route('/codigostatusdiferente')
def codigostatusdiferente():
    codigo = request.args['codigo']
    return f'<p>{codigo}</p>'

from flask import make_response
@app.route('/objetoresposta')
def objetoresposta():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

from flask import redirect
@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://ptb.ifsp.edu.br/')

from flask import abort
@app.route('/abortar')
def abortar():
    abort(404)
