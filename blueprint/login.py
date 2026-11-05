from flask import Blueprint,session,render_template,request,redirect,url_for,flash
from models.User import User
import hashlib
from sqlalchemy import and_
from extentions import db


login = Blueprint("login_blueprint",__name__)

@login.route("/")
def home():
    return render_template("login.html")

@login.route("/register",methods = ["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]

    if password != password2:
        flash("رمز اشتباه است")
        return redirect(url_for("login_blueprint.home"))

    check_user = User.query.filter(User.user_name == username).first()
    if check_user != None:
        flash("نام کاربری اشتباه است")
        return redirect(url_for("login_blueprint.home"))

    new_user = User(user_name = username,password = hashlib.sha256(password.encode()).hexdigest())
    db.session.add(new_user)
    db.session.commit()

    flash("ثبت نام موفقیت آمیز بود")
    return redirect(url_for("login_blueprint.home"))

@login.route("/login",methods = ["POST"])
def do_login():
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter(and_(User.user_name == username,User.password == hashlib.sha256(password.encode()).hexdigest() )).first()
    if user == None :
        flash("نام یا رمز شما اشتباه است")
        return redirect(url_for("login_blueprint.home"))
    
    session["login"] = username
    return redirect(url_for("panel_blueprint.home"))




    

    
