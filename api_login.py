FLASK_APP=Proyecto_Cloud.py
DATABASE_URI=postgresql://postgres:Ut3c-4536@localhost:5432/postgres

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

db.create_all() # Create sql tables for our data models (Usuario and Score)