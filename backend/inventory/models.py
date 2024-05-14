from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from inventory.database import Base

# class Product(Base):
#     __tablename__ = 'products'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     description = Column(Text)
#     date_added = Column(DateTime, default=datetime.now)
#     categories = relationship('Category', back_populates='product')

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'description': self.description,
#             'date_added': self.date_added.isoformat(),
#             'categories': [category.to_dict() for category in self.categories]
#         }
    
# class InventoryItem(Base):
#     __tablename__ = 'inventory_items'
#     id = Column(Integer, primary_key=True)
#     product_id = Column(Integer, ForeignKey('products.id'))
#     product = relationship('Product', uselist=False)
#     purchase_price = Column(Float, nullable=False)
#     date_added = Column(DateTime, default=datetime.now)
#     last_modified = Column(DateTime, default=datetime.now, onupdate=datetime.now)
#     supplier_id = Column(Integer, ForeignKey('suppliers.id')) #-could be bullshit "duplicate fields"
#     supplier = relationship('Supplier', uselist=False)

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'product': self.product.to_dict(),
#             'purchase_price': self.purchase_price,
#             'date_added': self.date_added.isoformat(),
#             'last_modified': self.last_modified.isoformat(),
#             'supplier': self.supplier.to_dict()
#         }
    
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    date_added = Column(DateTime, default=datetime.now)
    last_modified = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<User {self.name!r}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date_added': self.date_added.isoformat(),
            'last_modified': self.last_modified.isoformat(),
        }
    
# class Supplier(Base):
#     __tablename__ = 'suppliers'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     description = Column(Text)
#     address = Column(Text)
#     email = Column(String(120), nullable=False, unique=True)
#     contact_number = Column(String(20))
#     date_added = Column(DateTime, default=datetime.now)
#     last_modified = Column(DateTime, default=datetime.now, onupdate=datetime.now)

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'description': self.description,
#             'address': self.address,
#             'email': self.email,
#             'contact_number': self.contact_number,
#             'date_added': self.date_added.isoformat(),
#             'last_modified': self.last_modified.isoformat()
#         }