from flask import Blueprint
from app.controllers.JuegoController import profile, update

juego_bp = Blueprint('juego_bp', __name__)

juego_bp.route("/", methods=["GET"]) (profile)
juego_bp.route("/update", methods=["GET", "POST"]) (update)