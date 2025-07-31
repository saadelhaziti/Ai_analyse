import pandas as pd
from sqlalchemy import (
    create_engine, Column, Integer, String, Text, ForeignKey, Date, Numeric, TIMESTAMP
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# -----------------------
# Model Definitions
# -----------------------

class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    products = relationship("Product", back_populates="category")


class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String)
    shipping_address = Column(Text)
    billing_address = Column(Text)
    orders = relationship("Order", back_populates="customer")
    reviews = relationship("Review", back_populates="customer")
    payment_methods = relationship("PaymentMethod", back_populates="customer")


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Numeric, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    category = relationship("Category", back_populates="products")
    reviews = relationship("Review", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    order_date = Column(TIMESTAMP)
    status = Column(String, nullable=False)
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Numeric)
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")


class PaymentMethod(Base):
    __tablename__ = 'payment_methods'
    payment_method_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    card_number = Column(String, nullable=False)
    expiration_date = Column(Date, nullable=False)
    cvv = Column(String, nullable=False)
    customer = relationship("Customer", back_populates="payment_methods")


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    rating = Column(Integer)
    comment = Column(Text)
    timestamp = Column(TIMESTAMP)
    product = relationship("Product", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

# -----------------------
# Seeding function
# -----------------------

def seed_table(session, model, file_path, column_names):
    df = pd.read_csv(file_path, header=None, names=column_names)
    df = df.where(pd.notnull(df), None)
    records = [model(**row) for row in df.to_dict(orient='records')]
    session.bulk_save_objects(records)
    session.commit()
    print(f"Seeded {model.__tablename__} from {file_path}")

# -----------------------
# Main execution
# -----------------------

def main():
    engine = create_engine("postgresql://postgres:admin@db:5432/dbinit")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    seed_table(session, Category, 'retail_db/categories.csv', ['category_id', 'name'])
    seed_table(session, Customer, 'retail_db/customers.csv', [
        'customer_id', 'first_name', 'last_name', 'email',
        'phone_number', 'shipping_address', 'billing_address'
    ])
    seed_table(session, Product, 'retail_db/products.csv', [
        'product_id', 'name', 'description', 'price', 'stock_quantity', 'category_id'
    ])
    seed_table(session, Order, 'retail_db/orders.csv', [
        'order_id', 'customer_id', 'order_date', 'status'
    ])
    seed_table(session, PaymentMethod, 'retail_db/payment_methods.csv', [
        'payment_method_id', 'customer_id', 'card_number', 'expiration_date', 'cvv'
    ])
    seed_table(session, OrderItem, 'retail_db/order_items.csv', [
        'order_item_id', 'order_id', 'product_id', 'quantity', 'subtotal'
    ])
    seed_table(session, Review, 'retail_db/reviews.csv', [
        'review_id', 'product_id', 'customer_id', 'rating', 'comment', 'timestamp'
    ])

    print("✅ PostgreSQL database created and seeded successfully.")

if __name__ == '__main__':
    main()
