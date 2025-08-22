
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <h1>Avaliação contínua: Aula 030</h1>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/user/Isabela Genuino/PT3033317/IFSP">Identificação</a></li>
            <li><a href="/contextorequisicao">Contexto da requisição</a></li></ul>'''

@app.route('/user/<name>/<pt>/<campus>')
def hello_user(name, pt, campus):
    return f'''
    <h1>Avaliação contínua: Aula 030</h1>
        <h2>Aluno: {name}</h2>
        <h2>Prontuário: {pt}</h2>
        <h2>Instituição: {campus}</h2>
        <p><a href="/">Voltar</a></p>'''

@app.route('/contextorequisicao')
def contextorequisicao():
    navegador = request.headers.get('User-Agent')
    ipPcRemoto = request.remote_addr
    host = request.host
    return f'''
        <h1>Avaliação contínua: Aula 030</h1>
        <h2>Seu navegador é: {navegador}</h2>
        <h2>O IP do computador remoto é: {ipPcRemoto}</h2>
        <h2>O host da aplicação é: {host}</h2>
        <p><a href="/">Voltar</a></p>'''
