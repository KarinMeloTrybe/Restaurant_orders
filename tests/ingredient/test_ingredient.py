from src.models.ingredient import Ingredient


def test_ingredient():
    component_1 = Ingredient("LACTOSE")
    component_2 = Ingredient("GLUTEN")

    assert component_1 == component_1
    assert component_1 != component_2
    assert repr(component_1) == "Ingredient('LACTOSE')"
    assert hash(component_1) == hash("LACTOSE")
    assert component_1.restrictions == set()
    assert component_1.name == "LACTOSE"
