from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Transaction
from .forms import TransactionForm
from datetime import datetime
from collections import defaultdict

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    form = TransactionForm()
    transactions = Transaction.query.all()

    for t in transactions:
        t.amount = int(t.amount)

    grouped_transactions = defaultdict(list)
    for transaction in transactions:
        year_month = transaction.get_year_month()
        grouped_transactions[year_month].append(transaction)

    if form.validate_on_submit():
        transaction_type = form.type.data
        category = form.category.data
        amount = int(form.amount.data)
        date_str = request.form["date"]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

        new_transaction = Transaction(
            type=transaction_type, category=category, amount=amount, date=date_obj
        )
        db.session.add(new_transaction)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template(
        "index.html", form=form, grouped_transactions=grouped_transactions
    )


@main.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    form = TransactionForm()

    if form.validate_on_submit():
        transaction.type = form.type.data
        transaction.category = form.category.data
        transaction.amount = int(form.amount.data)
        date_str = request.form["date"]
        transaction.date = datetime.strptime(date_str, "%Y-%m-%d").date()

        db.session.commit()
        return redirect(url_for("main.index"))

    form.type.data = transaction.type
    form.category.data = transaction.category
    form.amount.data = int(transaction.amount)
    form.date.data = transaction.date

    return render_template("edit_transaction.html", form=form)


@main.route("/delete/<int:transaction_id>")
def delete(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for("main.index"))
