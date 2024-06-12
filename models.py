from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cryptocurrency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Cryptocurrency('{self.name}', '{self.symbol}', {self.price})"

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cryptocurrency_id = db.Column(db.Integer, db.ForeignKey('cryptocurrency.id'))
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"Transaction('{self.amount}', {self.timestamp})"

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cryptocurrency_id = db.Column(db.Integer, db.ForeignKey('cryptocurrency.id'))
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Wallet('{self.balance}')"
