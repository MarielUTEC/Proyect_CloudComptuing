from flask import Flask,request,jsonify, render_template
import datetime
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import json

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Config:
    # Obtener la clave secreta de la variable de entorno SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Obtener la URI de la base de datos de la variable de entorno DATABASE_URI
    DATABASE_URI = os.getenv('DATABASE_URI')

db = SQLAlchemy()
database_path=Config.DATABASE_URI
#Ejemplo: DATABASE_URI=postgresql://postgres:123@localhost:5432/utecmovie2023
# por el momento el database name lo trabajaremos en postgres.
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    with app.app_context():
        db.init_app(app)
        db.create_all()
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    score = db.relationship('Score', backref='user', lazy='dynamic')


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Princesa4'
    setup_db(app)

    @app.route('/login',methods=["GET","POST"])
    def login():
        body = request.get_json()
        print(body)
        username=body["username"] 
        password=body["password"]
        try:
            user = Usuario.query.filter(Usuario.username == username).first()
            if user == None or password != Usuario.password:
                return json.dumps({"success": False})
            else:
                return json.dumps({"success": True, "username": Usuario.username})
        except:
            return json.dumps({"success": False, "username": Usuario.username})

