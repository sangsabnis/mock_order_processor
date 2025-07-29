class Order:
    def __init__(self,order_id,customer_id,product_id,quantity,discount):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.discount = discount

    def __str__(self):
        return (f"Order(order_id='{self.order_id}', customer_id='{self.customer_id}', "
                f"product_id='{self.product_id}', quantity='{self.quantity}',  discount='{self.discount}')")