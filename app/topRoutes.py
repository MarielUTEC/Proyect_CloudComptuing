from app import app
import json
from flask import request, render_template
from app import db
from app.models import Usuario


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'usuario'}
    return render_template('index.html', title='Home', user=user, elemento1="codigo", elemento2="HTML")
@app.route('/indexdinamico', methods=['GET'])
def indexDinamico():
    args = request.args
    title = args.get("title")
    username = args.get("username")
    user = {'username': username}
    return render_template('index.html', title=title, user=user)

@app.route("/users")
def getAllUsers():
    users = Usuario.query.all()
    print(users)
    userStrings = ""
    for user in users:
        userStrings += user.dni + " " + user.password + " " + user.email + "<br>"
    return userStrings



#acceso al usaurio
 