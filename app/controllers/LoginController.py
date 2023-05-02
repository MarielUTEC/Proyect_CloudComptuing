from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Usuario,Puntos
import datetime

def getLogins():
    logins = Login.query.all()
    return logins

def Login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = Usuario.query.filter(Usuario.username == username).first()

        if user == None:
            return "Este usuario no existe :("
        if user.password != password:
            return "Contraseña Incorrecta.Intente nuevamente"
        
        return render_template("profile.html",username1 = username)

    return render_template("login.html")


def option():
    if request.method == "POST":
        points  = request.points["points"]
        id = request.id["points"]

        game = Usuario.quey.filter(Usuario.id == id).first()

        if game == None: 
            return "Este usuario no tiene un puntaje aún"
        if game.points > game.points: 
            return game