from distutils.log import Log
from flask import Blueprint
from app.controllers.LoginController import Login,getLogins
login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (Login)
login_bp.route("/getall", methods=["POST"]) (getLogins)
