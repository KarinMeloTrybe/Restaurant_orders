from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    ingredient1 = "presunto"
    ingredient2 = "farinha"
    ingredient3 = "frango"
    ingredient4 = "bacon"
    ingredient1_price = 10.00
    ingredient2_price = 5.00

    with pytest.raises(TypeError):
        Dish(ingredient1, "value")

    with pytest.raises(ValueError):
        Dish(ingredient1, 0)

    instance1 = Dish(ingredient2, ingredient2_price)
    instance2 = Dish(ingredient2, ingredient2_price)
    instance3 = Dish(ingredient1, ingredient1_price)
    item = Ingredient("frango")
    item2 = Ingredient("bacon")
    instance1.add_ingredient_dependency(item, 10)
    instance1.add_ingredient_dependency(item2, 5)

    assert hash(instance1) == hash(instance2)
    assert hash(instance1) != hash(instance3)
    assert instance1.__eq__(instance2) is True
    assert instance1.__eq__(instance3) is False
    assert instance1.get_ingredients() == {
        Ingredient(ingredient3),
        Ingredient(ingredient4)
    }
    assert instance1.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED
    }
    assert instance1.name == ingredient2
    assert repr(instance1) == f"Dish('{ingredient2}', R${ingredient2_price}0)"
