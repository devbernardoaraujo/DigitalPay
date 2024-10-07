import requests
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.models.users import Users

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
                # Se o usuário está logado, redireciona para /transactions
                return redirect(url_for('transactions'))
    

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Todos os campos são obrigatórios!", "danger")
            return redirect(url_for('login'))

        user = Users.query.filter_by(email=email).first()
        if user and user.check_password(password):
            flash("Login realizado com sucesso!", "success")
            login_user(user)
            # session of user
            return redirect(url_for('transactions'))
        else:
            flash("Email ou senha inválidos, tente novamente.", "danger")
            return redirect(url_for('login'))

    return render_template('authentication-login.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not email or not password:
            flash("Todos os campos são obrigatórios!", "danger")
            return redirect(url_for('register'))

        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            flash("O email já está em uso, por favor escolha outro.", "danger")
            return redirect(url_for('register'))

        new_user = Users(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Usuário registrado com sucesso!", "success")
        return redirect(url_for('login'))

    return render_template('authentication-register.html')

@app.route("/logout")
def logout():
    logout_user()
    return render_template('authentication-login.html')
