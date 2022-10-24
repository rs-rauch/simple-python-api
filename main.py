from flask import Flask, json, jsonify

meals = [{"name": "Spaghetti Carbonara", "price": 7.99, "origin": "Italy", "type": "pasta", "emoji": "🍝", "ingredients": ["egg", "bacon", "parmesan", "spaghetti"], "calories": 500},
         {"name": "Chicken Tikka Masala", "price": 8.99, "origin": "India", "type": "curry",
             "emoji": "🍛", "ingredients": ["chicken", "spices", "tomato", "cream"], "calories": 600},
         {"name": "Burger", "price": 5.99, "origin": "Germany", "type": "fast food",
             "emoji": "🍔", "ingredients": ["beef", "bun", "cheese", "lettuce"], "calories": 700},
         {"name": "Pancakes", "price": 6.99, "origin": "France", "type": "breakfast",
             "emoji": "🥞", "ingredients": ["eggs", "flour", "sugar", "butter"], "calories": 800},
         {"name": "Pizza", "price": 6.99, "origin": "Italy", "type": "fast food", "emoji": "🍕",
             "ingredients": ["dough", "cheese", "tomato", "pepperoni"], "calories": 900},
         {"name": "Lasagna", "price": 7.99, "origin": "Italy", "type": "pasta", "emoji": "🍝",
             "ingredients": ["beef", "cheese", "spices", "tomato"], "calories": 500},
         {"name": "Risotto", "price": 8.99, "origin": "Italy", "type": "pasta", "emoji": "🍝",
             "ingredients": ["rice", "cheese", "spices", "tomato"], "calories": 600},
         {"name": "Tiramisu", "price": 5.99, "origin": "Italy", "type": "dessert", "emoji": "🍰",
             "ingredients": ["eggs", "sugar", "coffee", "sponge cake "], "calories": 700},
         {"name": "Spaghetti Bolognese", "price": 6.99, "origin": "Italy", "type": "pasta",
             "emoji": "🍝", "ingredients": ["beef", "spices", "tomato", "spaghetti"], "calories": 800},
         {"name": "Pasta", "price": 6.99, "origin": "Italy", "type": "pasta", "emoji": "🍝", "ingredients": ["spaghetti", "tomato", "cheese", "basil"], "calories": 900}]


api = Flask(__name__)


@api.route('/', methods=['GET'])
def get_data():
    print("get all")
    return jsonify(meals)


if __name__ == '__main__':
    print("server ready")
    api.run(debug=True)
