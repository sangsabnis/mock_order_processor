
from models.order_item import OrderItem
from type_defs import ProductLookup


class Order:
    def __init__(self,order_id,customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = []


    def __str__(self):
        return (f"Order(order_id='{self.order_id}', customer_id='{self.customer_id}', "
                f"items='{self.items}')")

    def add_item(self, order_item: OrderItem):
        self.items.append(order_item)

    def total_items(self):
        return len(self.items)

    def subtotal(self, product_lookup: ProductLookup) -> float:
        subtotal = 0
        for item in self.items:
            product = product_lookup[item.product_id]
            subtotal += item.quantity * product.price
        return subtotal

    def total_tax(self, product_lookup: ProductLookup) -> float:
        result = sum(
            product_lookup[item.product_id].tax_rate * item.quantity * product_lookup[item.product_id].price
            for item in self.items
        )
        return round(result, 2)

    def total_discount(self, product_lookup: ProductLookup) -> float:
        result = sum(
            product_lookup[item.product_id].price * item.quantity * item.discount
            for item in self.items
        )
        return round(result, 2)

    def final_total(self, product_lookup: ProductLookup) -> float:
        return round(
            self.subtotal(product_lookup) +
            self.total_tax(product_lookup) -
            self.total_discount(product_lookup), 2)
