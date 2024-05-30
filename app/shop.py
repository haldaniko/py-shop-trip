from app.customer import Customer


class Shop:
    def __init__(self, name: str,
                 location: list[int],
                 products: dict):
        self.name = name
        self.location = location
        self.products = products

    def calculate_total_price(self, customer: Customer) -> int:
        return sum(self.products[product] * value
                   for product, value in customer.product_cart.items())
