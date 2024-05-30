import math
from app.car import Car


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list[int],
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_way_price(self, shop_location: list[int],
                            fuel_price: float) -> float:
        distance = math.sqrt(
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2
        )
        return round((distance / 100)
                     * self.car.fuel_consumption * 2 * fuel_price, 2)
