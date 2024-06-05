from abc import ABC, abstractmethod
from ast import literal_eval
import csv
from pprint import pprint


class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling=None):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price


class Regular(Cupcake):
    size = "regular"

    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"

    def calculate_price(self, quantity):
        return quantity * self.price

class Large(Cupcake):
    size = "large"

    def calculate_price(self, quantity):
        return quantity * self.price

mini_chocolate_delight = Mini("Chocolate Delight", 1.50, "Chocolate", "Chocolate Ganache")
mini_chocolate_delight.add_sprinkles("Chocolate Chips", "Gold Dust")

mini_vanilla_bean = Mini("Vanilla Bean", 1.50, "Vanilla", "Vanilla Buttercream")
mini_vanilla_bean.add_sprinkles("White Pearls")

large_red_velvet_surprise = Large("Red Velvet Surprise", 3.00, "Red Velvet", "Cream Cheese", "Cream Cheese Frosting")
large_red_velvet_surprise.add_sprinkles("Red Sugar", "Edible Glitter")

large_lemon_meringue = Large("Lemon Meringue", 3.00, "Lemon", "Lemon Curd", "Meringue")
large_lemon_meringue.add_sprinkles("Lemon Zest")

regular_strawberry_shortcake = Regular("Strawberry Shortcake", 2.50, "Strawberry", "Strawberry Jam", "Whipped Cream")
regular_strawberry_shortcake.add_sprinkles("Strawberry Slices", "Pink Sugar")

regular_caramel_crunch = Regular("Caramel Crunch", 2.50, "Caramel", "Caramel Sauce", "Caramel Buttercream")
regular_caramel_crunch.add_sprinkles("Toffee Bits")

regular_cookies_and_cream = Regular("Cookies and Cream", 2.50, "Chocolate", "Cookies and Cream", "Cookies and Cream Buttercream")
regular_cookies_and_cream.add_sprinkles("Crushed Oreos")


cupcake_list = [
    mini_chocolate_delight,
    mini_vanilla_bean,
    large_red_velvet_surprise,
    large_lemon_meringue,
    regular_caramel_crunch,
    regular_cookies_and_cream,
    regular_strawberry_shortcake,
]

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})



### Functions to add the cupcake dictionaries to file
def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        cupcakes = []
        for row in reader:
            row["price"] = float(row["price"])
            row["sprinkles"] = literal_eval(row["sprinkles"])
            cupcakes.append(row)
        return cupcakes

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

# write_new_csv("cupcakes.csv", cupcake_list)
read_csv("cupcakes.csv")
