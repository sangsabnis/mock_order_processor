class Customer:

    def __init__(self, id, name, region):
        self.id = id
        self.name = name
        self.region = region

    def __str__(self):
        return f"Customer(id='{self.id}', name='{self.name}', region='{self.region}')"