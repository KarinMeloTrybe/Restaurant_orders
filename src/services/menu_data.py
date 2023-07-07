from models.dish import Dish
from models.ingredient import Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.csv_data = pd.read_csv(source_path)
        b = False
        dishes = {
            name: Dish(name, price)
            for name, price, *data in self.csv_data.itertuples(index=b)
        }

        for name, _, ingredient, amount in self.csv_data.itertuples(index=b):
            ingredients = Ingredient(ingredient)
            dishes[name].add_ingredient_dependency(ingredients, amount)

        self.dishes.update(dishes.values())
