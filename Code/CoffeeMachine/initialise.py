from coffee_recipe.coffee_recipe import *
from copy import copy

americano = copy(recipe)
americano["Name"] = "Americano"
americano["Water"] = 100
americano["Beans"] = 10
americano["Milk"] = 0
americano["Cost"] = 3.5

espresso = copy(recipe)
espresso["Name"] = "Espresso"
espresso["Water"] = 10
espresso["Beans"] = 10
espresso["Milk"] = 0
espresso["Cost"] = 3.0

latte = copy(recipe)
latte["Name"] = "Latte"
latte["Water"] = 50
latte["Beans"] = 10
latte["Milk"] = 50
latte["Cost"] = 3.75

coffee_types = [americano,espresso,latte]
coffee_names = [drink["Name"] for drink in coffee_types]