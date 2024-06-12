from flask import render_template, request, redirect, url_for
from .models import Cryptocurrency, Transaction, Wallet

@app.route('/')
def index():
    cryptocurrencies = Cryptocurrency.query.all()
    return render_template('index.html', cryptocurrencies=cryptocurrencies)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        cryptocurrency_id = int(request.form['cryptocurrency_id'])
        amount = float(request.form['amount'])
        # Создайте транзакцию
        transaction = Transaction(cryptocurrency_id=cryptocurrency_id, amount=amount)
        db.session.add(transaction)
        db.session.commit()
        return redirect(url_for('wallet'))
    else:
        cryptocurrencies = Cryptocurrency.query.all()
        return render_template('payment.html', cryptocurrencies=cryptocurrencies)

@app.route('/wallet')
def wallet():
    wallet = Wallet.query.first()
    return render_template('wallet.html', wallet=wallet)
