from flask import Blueprint

from app.controllers.RegisterController import Register, registerasync
from app.controllers.LoginController import Login, loginasync, register

register_bp = Blueprint('register_bp', __name__)

register_bp.route("/", methods=["GET", "POST"]) (Register)
register_bp.route("/async", methods=["GET", "POST"]) (registerasync)

login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (Login)
login_bp.route("/async", methods=["GET", "POST"]) (loginasync)
login_bp.route("/register", methods=["GET","POST"]) (register)