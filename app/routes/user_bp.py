from flask import Blueprint

from app.controllers.UserController import Register, Points 

user_bp = Blueprint('user_bp', __name__)

user_bp.route("/register", methods=["GET", "POST"]) (Register)
user_bp.points("/points", methos = ["GET", "POST"]) (Points)