class Product:
    def __init__(self, id, name, price, tax_rate):
        self.id = id
        self.name = name
        self.price = float(price)
        self.tax_rate = float(tax_rate)

    def __str__(self):
        return f"Product(id='{self.id}', name='{self.name}', price='{self.price}', tax_rate='{self.tax_rate}')"