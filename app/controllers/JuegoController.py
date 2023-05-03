from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Usuario


def profile():
    user = request.args
    username = user.get("username")
    password = user.get("password")
    email = user.get("email")
    return render_template("profile.html", username=username, password=password, email=email)

def update():
    if request.method == "POST":
        usernameUpdate = request.form["username-update"]
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]

        if not username and not email and not password:
            return "Requires at least one parameter to update"
        user = Usuario.query.filter(Usuario.username==usernameUpdate).first()
        if user == None:
            return "Usuario Invalido"
        
        if username:
            user.username = username
        if password:
            user.password = password
        if email:
            user.email = email
        
        try:
            db.session.commit()
        except Exception as err:
            print("Error while updating", err)
            return "Internal error while updating, please try again"
        return redirect("/login")
    return render_template("update.html")