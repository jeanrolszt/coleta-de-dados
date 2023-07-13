from datetime import datetime  
from flask import Flask, flash, render_template, request, redirect
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
=======
import csv
>>>>>>> parent of 8200f46 (Adicionei conexão com o SQLite)
import os

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'asdasdasdasd'

<<<<<<< HEAD
# Google Cloud SQL config
# https://www.geeksforgeeks.org/setting-up-google-cloud-sql-with-flask/
# https://www.youtube.com/watch?v=Z4pzWi_470s
# https://github.com/GoogleCloudPlatform/getting-started-python/issues/129
# https://cloud.google.com/sql/docs/debugging-connectivity?hl=pt-br
# https://stackoverflow.com/questions/10763171/can-sqlalchemy-be-used-with-google-cloud-sql
# drop tables nome_table;
USER = "mtsousa" # Usuário de acesso
PASSWORD = "mtsousa123" # Senha do usuário
PUBLIC_IP_ADDRESS = "34.151.213.151" # IP público (no overview da instância)
DBNAME = "cadastro" # Nome do banco de dados
SOCKET_NAME = "virtual-conference-2022:southamerica-east1:cadastro-db" # Endereço de conexão

## https://github.com/GoogleCloudPlatform/getting-started-python/issues/129#issuecomment-548525780
if app.debug == False:
    app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+pymysql://{USER}:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{SOCKET_NAME}"
else:
    app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+pymysql://{USER}:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}"

# app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

db = SQLAlchemy(app)

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome_completo = db.Column(db.String(256), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    estado = db.Column(db.String(30), nullable=False)
    cargos = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.String(30), nullable=False)
    ip = db.Column(db.String(50), nullable=False)
    uas = db.Column(db.String(256), nullable=False)

    def __init__(self, nome_completo, cpf, telefone, email, estado, cargos, timestamp, ip, uas):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.estado = estado
        self.cargos = cargos
        self.timestamp = timestamp
        self.ip = ip
        self.uas = uas

with app.app_context():
    db.create_all()
=======
if not os.path.isfile(r"data.csv"):
        with open('data.csv', 'a', encoding='UTF8', newline='') as f:
            # create the csv writer
            writer = csv.writer(f, delimiter=';')
            data = ['nome completo','cpf','telefone','email','cargos','data','ip','browser','version','platform','uas']
            # write a row to the csv file
            writer.writerow(data)
>>>>>>> parent of 8200f46 (Adicionei conexão com o SQLite)

@app.route("/")
def coleta():
    return render_template('coleta.html')

@app.route("/registrar", methods=['POST'])
def registrar():
<<<<<<< HEAD
    nome_completo = request.form['nomeCompleto'][:255]
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    email = request.form['email'][:255]
    estado = request.form['estado']
    cargos = ','.join(x.upper() for x in list(request.form.keys())[5:])
    timestamp = datetime.utcnow() # UTC
    ip = request.remote_addr
    uas = str(request.user_agent.string)[:255]

    data = Usuarios(nome_completo, cpf, telefone, email, estado, cargos, timestamp, ip, uas)
    db.session.add(data)
    db.session.commit()

=======
    ip = request.remote_addr
    browser = request.user_agent.browser
    version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
    platform = request.user_agent.platform
    uas = request.user_agent.string
    timestamp = datetime.timestamp(datetime.now())

    # get the offices
    offices = ','.join(x.upper() for x in list(request.form.keys())[4:])

    # convert the timestamp to a datetime object in the local timezone
    dt_object = datetime.fromtimestamp(timestamp)
    with open('data.csv', 'a', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f, delimiter=';')
        data = [request.form['nomeCompleto'],request.form['cpf'],request.form['telefone'],request.form['email'],offices,dt_object,ip, browser, version, platform, uas]
        
        # write a row to the csv file
        writer.writerow(data)
    
>>>>>>> parent of 8200f46 (Adicionei conexão com o SQLite)
    flash('Obrigado por se registrar!')
    return redirect('/', 302)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))