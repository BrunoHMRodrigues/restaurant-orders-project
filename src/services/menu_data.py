import csv
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 3

class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.load_data_from_csv()
    
    def load_data_from_csv(self):
        with open(self.source_path, newline='') as csvfile:
            data_file = csv.reader(csvfile)

            # pular header
            next(data_file, None)

            # dish_data = {
            #     dish_name1: {
            #         price,
            #         ingredients: {
            #             ingredient1: amount,
            #             .
            #             .
            #             .
            #         }
            #     },
            #     dish_name2: {
            #         price,
            #         ingredients: {
            #             ingredient1: amount,
            #             .
            #             .
            #             .
            #         }
            #     },
            # }
            dish_data = {}
            for row in data_file:
                dish_name, dish_price, ingredient_name, ingredient_amount = row
                if dish_name not in dish_data:
                    dish_data[dish_name] = {
                        'price': float(dish_price),
                        'ingredients': {}
                    }
                dish_data[dish_name]['ingredients'][ingredient_name] = int(ingredient_amount)

            for dish_name, data in dish_data.items():
                dish = Dish(dish_name, data['price'])
                for ingredient_name, amount in data['ingredients'].items():
                    ingredient = Ingredient(ingredient_name)
                    dish.add_ingredient_dependency(ingredient, amount)
                self.dishes.add(dish)
