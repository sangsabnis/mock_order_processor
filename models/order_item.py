class OrderItem:
    def __init__(self,product_id,quantity,discount):
        self.product_id = product_id
        self.quantity = int(quantity)
        self.discount = float(discount)

    def __str__(self):
        return f"OrderItem(product_id:'{self.product_id}', quantity:'{self.quantity}', discount:'{self.discount}')"