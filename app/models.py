from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Transaction {self.type} - {self.category} - {self.amount}>"

    def get_year_month(self):
        return self.date.strftime("%Y-%m")

    def get_type_display(self):
        return "收入" if self.type == "收入" else "支出"

    def get_category_display(self):
        categories = {
            "food": "食物",
            "transport": "交通",
            "entertainment": "娛樂",
            "other": "其他",
        }
        return categories.get(self.category, "其他")

    def get_date_display(self):
        return self.date.strftime("%Y-%m-%d")

    def get_date_for_form(self):
        return self.date.strftime("%Y-%m-%d")
