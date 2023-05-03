from flask import Blueprint

from app.controllers.RegisterController import Register 

register_bp = Blueprint('register_bp', __name__)

register_bp.route("/", methods=["GET", "POST"]) (Register)