from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    SubmitField,
    DateField,
    IntegerField,
)
from wtforms.validators import DataRequired


class TransactionForm(FlaskForm):
    type = SelectField(
        "類型",
        choices=[("收入", "收入"), ("支出", "支出")],
        validators=[DataRequired()],
    )
    category = SelectField(
        "類別",
        choices=[
            ("薪水", "薪水"),
            ("兼職", "兼職"),
            ("投資收益", "投資收益"),
            ("其他", "其他"),
            ("交通", "交通"),
            ("食物", "食物"),
            ("娛樂", "娛樂"),
            ("住房", "住房"),
            ("水電", "水電"),
            ("保險", "保險"),
            ("教育", "教育"),
            ("醫療", "醫療"),
            ("購物", "購物"),
            ("旅遊", "旅遊"),
            ("健身", "健身"),
        ],
        validators=[DataRequired()],
    )
    amount = IntegerField("金額 (NT$)", validators=[DataRequired()])
    date = DateField(
        "日期",
        format="%Y-%m-%d",
        validators=[DataRequired()],
        render_kw={"class": "form-control", "style": "width: 135%; max-width: 350px;"},
    )
    submit = SubmitField("新增")
