from database import db, Base

order_product = db.Table(
    'Order_Product',
    Base.metadata,
    db.Column('oder_id', db.ForeignKey('Orders.id'), primary_key=True),
    db.Column('product_id', db.ForeignKey('Products.id'), primary_key=True)
)

