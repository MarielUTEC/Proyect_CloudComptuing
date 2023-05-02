
from cgitb import html
from turtle import position
from app import app
import re
from flask import render_template, request, redirect
from app import db
import datetime
from app.models import Usuario,Puntos

def Register():
    
    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]
        email = request.form["email"]
        password = request.form["password"]

        user = Usuario.query.filter(Usuario.username == username).first()

        if user != None:
            return "Usuario ya existente"

        newUser = Usuario(username=username,age = age,email = email,password = password)
        newPoints = Puntos(username=username,position = PuestoDefault(),corrects = 0,fails=0,points = 0)
        
        
        try:
            db.session.add(newUser)
            db.session.add(newPoints)
            db.session.commit()
            return render_template("back_index.html",username1 = newUser.username)
        except Exception as err:
            return "ERROR 404"
        
    return render_template("register.html")





def PuestoDefault():

    users = Usuario.query.all()
    cont = 0
    for user in users:
        if user:
            cont += 1
    
    puesto = cont + 1
    return puesto


        