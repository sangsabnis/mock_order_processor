from models.customer import Customer
from models.order import Order
from models.product import Product
from utils.csv_loader import load_csv_as_dict

print("Reading customers")
customers = []
for c in load_csv_as_dict('data/customers.csv'):
    customer = Customer(c["customer_id"], c["name"], c["region"])
    customers.append(customer)
for customer in customers:
    print(customer)

print("Reading products")
products = []
for p in load_csv_as_dict('data/products.csv'):
    product = Product(p["product_id"], p["name"], p["price"], p["tax_rate"])
    products.append(product)
for product in products:
    print(product)

print("Reading orders")
orders = []
for o in load_csv_as_dict('data/orders.csv'):
    order = Order(o["order_id"], o["customer_id"], o["product_id"], o["quantity"], o["discount"])
    orders.append(order)
for order in orders:
    print(order)