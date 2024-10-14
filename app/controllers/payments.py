import requests
from app import app, config
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.payments import Marketplaces
from app.models.pessoafisica import PessoaFisica

@app.route("/transactions", methods=["GET"])
@login_required
def transactions():
    marketplace = Marketplaces.query.filter_by(id=current_user.marketplace_id).first()

    if not marketplace:
        flash("Marketplace não encontrado.", "danger")
        return redirect(url_for('logout'))

    query_params = '?'

    res = requests.get(
        "{}/v1/marketplaces/{}/transactions".format(config.host, marketplace.external_id),
        auth=(marketplace.private_key, None),
    )

    transactions_list = res.json().get('items', [])
    total_pages = res.json().get('total_pages', 0)

    return render_template('transactions.html', transactions_list=transactions_list, total_pages=total_pages)

@app.route("/transactions/details", methods=["POST"])
@login_required
def transactions_details():
    marketplace = Marketplaces.query.filter_by(id=current_user.marketplace_id).first()

    if not marketplace:
        flash("Marketplace não encontrado.", "danger")
        return redirect(url_for('logout'))

    transaction = request.form.get("transaction")

    res = requests.get(
        "{}/v1/marketplaces/{}/transactions/{}".format(config.host, marketplace.external_id, transaction),
        auth=(marketplace.private_key, None),
    )

    transactions_list = [res.json()]
    total_pages = 0

    return render_template('transactions.html', transactions_list=transactions_list, total_pages=total_pages)


@app.route("/transfers", methods=["GET"])
@login_required
def transfers():
    marketplace = Marketplaces.query.filter_by(id=current_user.marketplace_id).first()

    if not marketplace:
        flash("Marketplace não encontrado.", "danger")
        return redirect(url_for('logout'))

    res = requests.get(
        "{}/v1/marketplaces/{}/sellers/{}/transfers".format(config.host, marketplace.external_id, config.seller),
        auth=(marketplace.private_key, None),
    )

    transfers_list = res.json().get('items', [])

    return render_template('transfers.html', transfers_list=transfers_list)


@app.route("/pessoafisica", methods=["GET", "POST"])
@login_required
def pessoa_fisica():
    if request.method == "POST":
        # obter dados do user no formulario
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        taxpayer_id = request.form.get("taxpayer_id")
        birthdate = request.form.get("birthdate")
        statement_descriptor = request.form.get("statement_descriptor")
        revenue = request.form.get("revenue")

        address = {
            "line1": request.form.get("line1"),
            "line2": request.form.get("line2"),
            "line3": request.form.get("line3"),
            "neighborhood": request.form.get("neighborhood"),
            "city": request.form.get("city"),
            "state": request.form.get("state"),
            "postal_code": request.form.get("postal_code"),
            "country_code": request.form.get("country_code"),
        }

        mcc = request.form.get("mcc")

        # processar dados enviados pelo user e chamar api da zoop
        marketplace = Marketplaces.query.filter_by(id=current_user.marketplace_id).first()

        if not marketplace:
            flash("Marketplace não encontrado.", "danger")
            return redirect(url_for('logout'))

        # payload para enviar para a api da zoop, apenas dei um crtl c + ctrl v
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
            "taxpayer_id": taxpayer_id,
            "birthdate": birthdate,
            "statement_descriptor": statement_descriptor,
            "revenue": revenue,
            "address": address,
            "mcc": mcc,
        }

        # chamando api da zoop conforme previsto na doc!
        url = f"https://api.zoop.ws/v1/marketplaces/{marketplace.external_id}/sellers/individuals"
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        res = requests.post(url, json=payload, headers=headers, auth=(marketplace.private_key, None))

        if res.status_code == 201:
            flash("Pessoa Física criada com sucesso!", "success")
            return redirect(url_for('transactions'))
        else:
            flash("Erro ao criar Pessoa Física: " + res.json().get("error", "Erro desconhecido"), "danger")
            return redirect(url_for('pessoa_fisica'))  # Corrigido para redirecionar para a rota

    # template de pessooafisica 
    return render_template('theme/pessoafisica-register.html')


