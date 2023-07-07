from csv import DictReader
import csv
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Dict:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    def load_inventory(self, inventory_path):
        inventory = {}
        with open(inventory_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                ingredient, quantity = row[0], int(row[1])
                inventory[ingredient] = quantity
        return inventory

        # Atualizar o arquivo CSV com o novo estoque (opcional)

        return None

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe):
        for ingredient, quantity in recipe.items():
            if (
                ingredient not in self.inventory
                or quantity > self.inventory[ingredient]
              ):
                return False
        return True

    # Req 5.2

    def consume_recipe(self, recipe: Recipe) -> None:
        if not self.check_recipe_availability(recipe):
            raise ValueError("Recipe not available")
        for ingredient, quantity in recipe.items():
            self.inventory[ingredient] -= quantity
