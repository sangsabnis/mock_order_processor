

from models.customer import Customer
from models.order import Order
from models.order_item import OrderItem
from models.product import Product
from utils.csv_loader import load_csv_as_dict

print("Reading customers")
customers = {}
for c in load_csv_as_dict('data/customers.csv'):
    customer = Customer(c["customer_id"], c["name"], c["region"])
    customers[customer.id] = customer
print(customers)

print("Reading products")
products = {}
for p in load_csv_as_dict('data/products.csv'):
    product = Product(p["product_id"], p["name"], p["price"], p["tax_rate"])
    products[product.id] = product
print(products)

print("Reading orders")
orders = {}
for o in load_csv_as_dict('data/orders.csv'):
    order_id = o["order_id"]
    order = orders.setdefault(order_id, Order(order_id, o["customer_id"]))
    order_item = OrderItem(o["product_id"], o["quantity"], o["discount"])
    order.add_item(order_item)
    orders[order_id] = order
print(orders)

for order_id in orders:
    order = orders[order_id]
    print(f"order {order_id} number of items {order.total_items()} subtotal {order.subtotal(products)}"
          f" total tax {order.total_tax(products)} total discount {order.total_discount(products)}")
    print(f"Final order total {order.final_total(products)}\n")