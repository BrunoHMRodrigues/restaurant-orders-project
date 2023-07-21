from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest

# Req 2


def test_dish():
    LASANHA = 'lasanha'
    LASANHA_PRICE = 26.00
    dish1 = Dish(LASANHA, LASANHA_PRICE)
    dish2 = Dish(LASANHA, 30.20)

    assert dish1.name == LASANHA
    assert dish1.price == LASANHA_PRICE
    assert dish1.recipe == {}

    # o método mágico __repr__ funcione como esperado;
    assert repr(dish1) == f'Dish("{LASANHA}", R${LASANHA_PRICE:.2f})'
    assert repr(dish1) == repr(dish1)
    assert repr(dish1) != repr(dish2)

    # o método mágico __eq__ funcione como esperado;
    assert dish1 == dish1
    assert dish1 != dish2

    # o método mágico __hash__ funcione como esperado.
    assert hash(repr(dish1)) == hash(repr(dish1))
    assert hash(repr(dish1)) != hash(repr(dish2))

    # Testando o método add_ingredient_dependency
    ingredient_presunto = Ingredient("presunto")
    dish1.add_ingredient_dependency(ingredient_presunto, 5)

    # Testando o método get_ingredients
    assert dish1.get_ingredients() == {ingredient_presunto}
    assert dish1.recipe.get(ingredient_presunto) == 5

    # Testando o método get_restrictions
    assert dish1.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED
    }

    # Testando TypeError quando prato com valor de tipo inválido
    with pytest.raises(TypeError):
        Dish(LASANHA, "invalid_price")

    # Testando ValueError quando prato com valor inválido
    with pytest.raises(ValueError):
        Dish(LASANHA, -10.0)
