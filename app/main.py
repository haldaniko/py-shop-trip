from app.customer import Customer
from app.shop import Shop
from app.car import Car

import json
import datetime


def get_from_json(location: str) -> tuple[list[Customer], list[Shop], float]:
    with open(location, "r") as file:
        data = json.load(file)

    customers = [Customer(customer["name"],
                          customer["product_cart"],
                          customer["location"],
                          customer["money"],
                          Car(customer["car"]["brand"],
                              customer["car"]["fuel_consumption"]))
                 for customer in data["customers"]]
    shops = [Shop(shop["name"],
                  shop["location"],
                  shop["products"])
             for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]
    return customers, shops, fuel_price


def shop_trip() -> None:
    customers, shops, fuel_price = get_from_json("app/config.json")

    for customer in customers:

        best_price = float("inf")
        best_shop = None
        home_location = customer.location

        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            way_price = customer.calculate_way_price(shop.location, fuel_price)
            shop_price = shop.calculate_total_price(customer)
            total_price = way_price + shop_price
            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {total_price}")
            if total_price < best_price:
                best_price = total_price
                best_shop = shop

        if customer.money >= best_price:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.location = best_shop.location
            _time = datetime.datetime.now()
            print(f"Date: {_time.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, value in customer.product_cart.items():
                cost_product = (best_shop.products[product]
                                * customer.product_cart[product])
                if int(cost_product) == cost_product:
                    print(f"{value} {product}s "
                          f"for {int(cost_product)} dollars")
                else:
                    print(f"{value} {product}s for {cost_product} dollars")
            print(f"Total cost is "
                  f"{best_shop.calculate_total_price(customer)} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.location = home_location
            print(f"{customer.name} now has "
                  f"{customer.money - best_price} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
