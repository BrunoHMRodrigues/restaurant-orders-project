from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501

# Req 1


def test_ingredient():
    BACON = 'bacon'
    FARINHA = 'farinha'

    ingredient1 = Ingredient(BACON)
    ingredient2 = Ingredient(BACON)
    ingredient3 = Ingredient(FARINHA)

    bacon_expected_restrictions = {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED
    }
    farinha_expected_restrictions = {Restriction.GLUTEN}

    assert ingredient1.name == BACON
    assert ingredient2.name == BACON
    assert ingredient3.name == FARINHA

    # o atributo conjunto restrictions é populado como esperado;
    assert ingredient1.restrictions == bacon_expected_restrictions
    assert ingredient3.restrictions == farinha_expected_restrictions

    # o método mágico __hash__ funcione como esperado.
    assert hash(ingredient1.name) == hash(ingredient2.name)
    assert hash(ingredient1.name) != hash(ingredient3.name)

    # o método mágico __repr__ funcione como esperado;
    assert repr(ingredient1) == 'Ingredient("bacon")'
    assert repr(ingredient3) == 'Ingredient("farinha")'

    # o método mágico __eq__ funcione como esperado;
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3
