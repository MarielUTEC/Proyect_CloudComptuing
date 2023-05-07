from flask import Blueprint
from app.controllers.LoginController import Login, loginasync, register
from app.controllers.JuegoController import profile, update

login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (Login)
login_bp.route("/async", methods=["GET", "POST"]) (loginasync)
login_bp.route("/register", methods=["GET","POST"]) (register)

juego_bp = Blueprint('juego_bp', __name__)

juego_bp.route("/", methods=["GET", "POST"]) (profile)
juego_bp.route("/update", methods=["GET", "POST"]) (update)
