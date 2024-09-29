import requests
from app import app, config, db
from flask import Flask, render_template, request, redirect, url_for, flash
from app.models.payments import Marketplaces, Users

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Todos os campos são obrigatórios!", "danger")
            return redirect(url_for('login'))
        
        user = Users.query.filter_by(email=email).first()
        if user and user.check_password(password):
            flash("Login realizado com sucesso!", "success")
            #session of user 
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

@app.route("/transactions", methods=["GET"])
def transactions():
    marketplace = Marketplaces.query.filter_by(external_id="c56526d5c795437aac54820edc297496").first()
    if not marketplace:
        flash("Marketplace não encontrado.", "danger")
        return redirect(url_for('hello'))

    res = requests.get(
        "{}/v1/marketplaces/{}/sellers/{}/transactions".format(config.host, marketplace.external_id, config.seller),
        auth=(marketplace.private_key, None),
    )

    transactions_list = res.json().get('items', [])
    total_pages = res.json().get('total_pages', 0)

    return render_template('transactions.html', transactions_list=transactions_list, total_pages=total_pages)

@app.route("/transfers", methods=["GET"])
def transfers():
    res = requests.get(
        "{}/v1/marketplaces/{}/sellers/{}/transfers".format(config.host, config.marketplace, config.seller),
        auth=(config.zpk, None),
    )

    transfers_list = res.json().get('items', [])

    return render_template('transfers.html', transfers_list=transfers_list)
