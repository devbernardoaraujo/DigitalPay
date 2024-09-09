from app import app, config, db
from flask import Flask, render_template

import requests

from app.models.payments import Marketplace
from app.models.payments import User



@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('authentication-login.html')

@app.route("/register", methods=["GET", "POST"])
def register():

    return render_template('authentication-register.html')

@app.route("/transactions", methods=["GET"])
def transactions():
    marketplace = Marketplace.query.filter_by(external_id="c56526d5c795437aac54820edc297496").all()[0]

    res = requests.get(
        "{}/v1/marketplaces/{}/sellers/{}/transactions".format(config.host,marketplace.external_id,config.seller),
        auth=(marketplace.private_key,None),
    )

    transactions_list = res.json()['items']
    total_pages = res.json()['total_pages']

    # page = res.json()['total_pages']
    # offset = res.json()['total_pages']

    return render_template('transactions.html', transactions_list=transactions_list, total_pages=total_pages)


@app.route("/transfers", methods=["GET"])
def transfers():
    res = requests.get(
        "{}/v1/marketplaces/{}/sellers/{}/transfers".format(config.host, config.marketplace, config.seller),
        auth=(config.zpk, None),
    )

    transfers_list = res.json()['items']

    # page = res.json()['total_pages']
    # offset = res.json()['total_pages']

    return render_template('transfers.html', transfers_list=transfers_list)