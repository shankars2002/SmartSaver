from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
transactions = []

@app.route('/')
def index():
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = income - expenses
    tip = "Use the 50/30/20 rule: 50% Needs, 30% Wants, 20% Savings."
    return render_template('index.html', transactions=transactions, income=income,
                           expenses=expenses, balance=balance, tip=tip)

@app.route('/add', methods=['POST'])
def add():
    t_type = request.form['type']
    description = request.form['description']
    amount = float(request.form['amount'])
    category = request.form['category']
    date = request.form['date']
    transactions.append({
        "type": t_type,
        "description": description,
        "amount": amount,
        "category": category,
        "date": date
    })
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
