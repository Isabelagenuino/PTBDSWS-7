
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def hello_world():
    return render_template('index.html', current_time = datetime.utcnow())

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
