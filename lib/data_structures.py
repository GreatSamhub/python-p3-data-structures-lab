spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names
print(get_names(spicy_foods))
pass
    

def get_spiciest_foods(spicy_foods):
    spiciest_foods = {}
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods[food["name"]] = food
    return spiciest_foods
print(get_spiciest_foods(spicy_foods))
pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
print(print_spicy_foods(spicy_foods))
pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
pass

def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
print(print_spiciest_foods(spicy_foods))
pass
def get_average_heat_level(spicy_foods):
    heat_level_sum = 0
    for food in spicy_foods:
        heat_level_sum += food["heat_level"]
    return heat_level_sum / len(spicy_foods)
print(get_average_heat_level(spicy_foods))
pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
print(create_spicy_food(spicy_foods, {"name": "Desert", "cuisine": "Kenyan", "heat_level": 10}))  
pass
