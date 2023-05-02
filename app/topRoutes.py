from app import app
import json
from flask import request, render_template
from app import db
from app.models import Usuario,Puntos

@app.route("/",methods = ["GET","POST"])
def Index():
    return render_template("index.html")



#acceso al usaurio
 