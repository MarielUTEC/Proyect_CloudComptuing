from distutils.log import Log
from flask import Blueprint
from app.controllers.LoginController import Login, loginasync, register
login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (Login)
login_bp.route("/register", methods=["GET","POST"]) (register)
login_bp.route("/loginasync", methods=["GET","POST"]) (loginasync)
