import pandas as pd
import uuid
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Parameters
NUM_CUSTOMERS = 100
NUM_PRODUCTS = 50
NUM_ORDERS = 200
MAX_ITEMS_PER_ORDER = 5
PAYMENT_METHODS = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery']

# 1. Customers
customers = []
for _ in range(NUM_CUSTOMERS):
    customers.append({
        'customer_id': str(uuid.uuid4()),
        'name': fake.name(),
        'email': fake.email(),
        'location': fake.city()
    })
df_customers = pd.DataFrame(customers)
df_customers.to_csv('customers.csv', index=False)

# 2. Products
categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys']
products = []
for _ in range(NUM_PRODUCTS):
    products.append({
        'product_id': str(uuid.uuid4()),
        'product_name': fake.word().capitalize(),
        'category': random.choice(categories),
        'price': round(random.uniform(10, 500), 2)
    })
df_products = pd.DataFrame(products)
df_products.to_csv('products.csv', index=False)

# 3. Orders
orders = []
for _ in range(NUM_ORDERS):
    orders.append({
        'order_id': str(uuid.uuid4()),
        'customer_id': random.choice(df_customers['customer_id']),
        'order_date': fake.date_between(start_date='-1y', end_date='today').isoformat()
    })
df_orders = pd.DataFrame(orders)
df_orders.to_csv('orders.csv', index=False)

# 4. Order Items
order_items = []
for order in df_orders.itertuples():
    for _ in range(random.randint(1, MAX_ITEMS_PER_ORDER)):
        order_items.append({
            'order_item_id': str(uuid.uuid4()),
            'order_id': order.order_id,
            'product_id': random.choice(df_products['product_id']),
            'quantity': random.randint(1, 5)
        })
df_order_items = pd.DataFrame(order_items)
df_order_items.to_csv('order_items.csv', index=False)

# 5. Payments
payments = []
for order in df_orders.itertuples():
    amount = sum(
        df_products[df_products['product_id'] == item['product_id']]['price'].values[0] * item['quantity']
        for item in df_order_items[df_order_items['order_id'] == order.order_id].to_dict('records')
    )
    payments.append({
        'payment_id': str(uuid.uuid4()),
        'order_id': order.order_id,
        'amount': round(amount, 2),
        'payment_method': random.choice(PAYMENT_METHODS)
    })
df_payments = pd.DataFrame(payments)
df_payments.to_csv('payments.csv', index=False)
