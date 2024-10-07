import requests
from app import app, config
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.payments import Marketplaces

@app.route("/transactions", methods=["GET"])
@login_required
def transactions():
    marketplace = Marketplaces.query.filter_by(external_id="c56526d5c795437aac54820edc297496").first()
    if not marketplace:
        flash("Marketplace não encontrado.", "danger")
        return redirect(url_for('logout'))

    res = requests.get(
        "{}/v1/marketplaces/{}/sellers/{}/transactions".format(config.host, marketplace.external_id, config.seller),
        auth=(marketplace.private_key, None),
    )

    transactions_list = res.json().get('items', [])
    total_pages = res.json().get('total_pages', 0)

    return render_template('transactions.html', transactions_list=transactions_list, total_pages=total_pages)

@app.route("/transfers", methods=["GET"])
def transfers():
    marketplace = Marketplaces.query.filter_by(external_id="c56526d5c795437aac54820edc297496").first()
    if not marketplace:
        flash("Marketplace não encontrado.", "danger")
        return redirect(url_for('logout'))

    res = requests.get(
        "{}/v1/marketplaces/{}/sellers/{}/transfers".format(config.host, marketplace.external_id, config.seller),
        auth=(marketplace.private_key, None),
    )

    transfers_list = res.json().get('items', [])

    return render_template('transfers.html', transfers_list=transfers_list)
