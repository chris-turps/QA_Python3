recipe = {
            "Name":""
            , "Water":0
            , "Beans":0
            , "Milk":0
            , "Cost":0
        }

class Drink:
    def __init__(self
        , drink_name
        , water_ml
        , beans_g
        , milk_ml
        , cost_p
        ):
        self.name = drink_name
        self.water = water_ml
        self.beans = beans_g
        self.milk = milk_ml
        self.cost = cost_p

    def __str__(self) -> str:
        return f'Name: {self.name}, Water: {self.water}'