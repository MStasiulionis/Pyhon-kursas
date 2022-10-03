from sqlalchemy import Column, Integer, String, Float

from Flaskas.prekiu_uzsakymas.db import db


class Products(db.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_name = Column("name", String(100), nullable=False)
    product_price = Column("price", Float(10), nullable=False)
    amount = Column("amount", Integer(), nullable=False)
