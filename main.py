from datetime import datetime  
from flask import Flask, flash, render_template, request, jsonify
import os
import pymysql
from flask import Flask
import re


app = Flask(__name__)

mysql = pymysql.connect(host="localhost", port=3377, user="root", password="r00t", database="coleta")


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'minhachavesecretaetop'

@app.route("/")
def coleta():
    return render_template('coleta.html')

@app.route("/registrar", methods=['POST'])
def registrar():
    ip = request.remote_addr
    browser = request.user_agent.browser
    version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
    platform = request.user_agent.platform
    uas = request.user_agent.string
    cpf = re.sub('[^0-9]', '', request.form['cpf'])
    with mysql.cursor() as cur:
        cur.execute("INSERT INTO pessoas_partido_historico (`nome`, `cpf`, `email`, `telefone`, `ip`)  values(%s,%s,%s,%s,%s)", (request.form['nomeCompleto'], cpf, request.form['email'], request.form['telefone'], ip))
        cur.connection.commit()
    return render_template('horario.html')

@app.route("/horario")
def horario():
    return render_template('horario.html')


@app.route("/pessoa/<cpf>")
def getPessoaByCpf(cpf):

    cpf = re.sub('[^0-9]', '', cpf)
    sql = 'SELECT * FROM pessoas_partido WHERE {} = %s'

    try:
        with mysql.cursor() as cur:
            cur.execute(sql.format("cpf"), (cpf,))
            result = cur.fetchmany(1)
            print(result)
            nome = result[0][1]
            cpf = result[0][2]
            email = result[0][3]
            telefone = result[0][6]
            response = jsonify(nome=nome, cpf=cpf, email=email, telefone=telefone)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
    except:
        response = jsonify(status=404, msg="Pessoa não encontrada")
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8444)