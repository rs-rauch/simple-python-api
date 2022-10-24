from flask import Flask, jsonify, request


# list of meals
meals = {
    1: {"name": "Spaghetti Carbonara", "price": 7.99, "origin": "Italy", "type": "pasta",
        "emoji": "🍝", "ingredients": ["egg", "bacon", "parmesan", "spaghetti"], "calories": 500},
    2: {"name": "Chicken Tikka Masala", "price": 8.99, "origin": "India", "type": "curry",
        "emoji": "🍛", "ingredients": ["chicken", "spices", "tomato", "cream"], "calories": 600},
    3: {"name": "Burger", "price": 5.99, "origin": "Germany", "type": "fast food",
        "emoji": "🍔", "ingredients": ["beef", "bun", "cheese", "lettuce"], "calories": 700},
    4: {"name": "Pancakes", "price": 6.99, "origin": "France", "type": "breakfast",
        "emoji": "🥞", "ingredients": ["eggs", "flour", "sugar", "butter"], "calories": 800},
    5: {"name": "Pizza", "price": 6.99, "origin": "Italy", "type": "fast food",
        "emoji": "🍕", "ingredients": ["dough", "cheese", "tomato", "pepperoni"], "calories": 900},
    6: {"name": "Lasagna", "price": 7.99, "origin": "Italy", "type": "pasta",
        "emoji": "🍝", "ingredients": ["beef", "cheese", "spices", "tomato"], "calories": 500},
    7: {"name": "Risotto", "price": 8.99, "origin": "Italy", "type": "pasta",
        "emoji": "🍝", "ingredients": ["rice", "cheese", "spices", "tomato"], "calories": 600},
    8: {"name": "Tiramisu", "price": 5.99, "origin": "Italy", "type": "dessert",
        "emoji": "🍰", "ingredients": ["eggs", "sugar", "coffee", "sponge cake "], "calories": 700},
    9: {"name": "Spaghetti Bolognese", "price": 6.99, "origin": "Italy", "type": "pasta",
        "emoji": "🍝", "ingredients": ["beef", "spices", "tomato", "spaghetti"], "calories": 800},
    10: {"name": "Pasta", "price": 6.99, "origin": "Italy", "type": "pasta",
         "emoji": "🍝", "ingredients": ["spaghetti", "tomato", "cheese", "basil"], "calories": 900}
}

# recepies for the meals with text and step-by-step instructions
recipes = {
    1: {
        "title": "Spaghetti Carbonara",
        "text": "Pasta with bacon, eggs and parmesan cheese.",
        "steps": [
            "Cook pasta in salted water.",
            "Fry bacon and chop it.",
            "Beat the eggs with the parmesan cheese.",
            "Mix the pasta with the bacon and the egg mixture."
        ]
    },
    2: {
        "title": "Chicken Tikka Masala",
        "text": "Chicken in a creamy tomato sauce with spices.",
        "steps": [
            "Heat oil in a pan and fry the chicken.",
            "Add the spices, tomatoes and cream and cook for 15 minutes."
        ]
    },
    3: {
        "title": "Burger",
        "text": "Beef patty with cheese, lettuce and tomato.",
        "steps": [
            "Grill the beef patty.",
            "Add cheese, lettuce and tomato."
        ]
    },
    4: {
        "title": "Pancakes",
        "text": "Fluffy pancakes with butter and syrup.",
        "steps": [
            "Mix the eggs, flour, sugar and milk.",
            "Fry the pancakes on both sides."
        ]
    },
    5: {
        "title": "Pizza",
        "text": "Pizza with tomato sauce, cheese and pepperoni.",
        "steps": [
            "Roll out the dough.",
            "Spread tomato sauce on the dough.",
            "Add cheese and pepperoni."
        ]
    },
    6: {
        "title": "Lasagna",
        "text": "Pasta with beef, tomato sauce and cheese.",
        "steps": [
            "Cook pasta in salted water.",
            "Fry the beef and add the tomato sauce.",
            "Mix the pasta with the beef and the tomato sauce and add the cheese."
        ]
    },
    7: {
        "title": "Risotto",
        "text": "Rice with tomato sauce and cheese.",
        "steps": [
            "Cook the rice in salted water.",
            "Fry the onion and garlic and add the tomato sauce.",
            "Add the rice to the tomato sauce and cook for 15 minutes."
        ]
    },
    8: {
        "title": "Tiramisu",
        "text": "Coffee-flavoured dessert with sponge cake and eggs.",
        "steps": [
            "Mix the eggs with the sugar.",
            "Soak the sponge cake in coffee.",
            "Mix the sponge cake with the egg mixture."
        ]
    },
    9: {
        "title": "Spaghetti Bolognese",
        "text": "Pasta with beef, tomato sauce and cheese.",
        "steps": [
            "Cook pasta in salted water.",
            "Fry the beef and add the tomato sauce.",
            "Mix the pasta with the beef and the tomato sauce and add the cheese."
        ]
    },
    10: {
        "title": "Pasta",
        "text": "Pasta with tomato sauce, cheese and basil.",
        "steps": [
            "Cook pasta in salted water.",
            "Fry the onion and garlic and add the tomato sauce.",
            "Mix the pasta with the tomato sauce and add the cheese."
        ]
    }
}

# unique reviews with rating and comment for the meals
reviews = {
    1: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ],
    2: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ],
    3: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ],
    4: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ],
    5: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ],
    6: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ],
    7: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ],
    8: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ],
    9: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ],
    10: [
        {"rating": 4, "comment": "Delicious!"},
        {"rating": 5, "comment": "Yummy!"},
        {"rating": 4, "comment": "Great!"},
        {"rating": 4, "comment": "Awesome!"}
    ]
}


api = Flask(__name__)

# get all meals


@api.route('/meals', methods=['GET'])
def get_meal_data():
    """get all meals

    Return: list of meals
    """

    return jsonify(meals)

# get a specific meal


@api.route('/meals/<int:id>', methods=['GET'])
def get_meal(id):
    """Get a specific meal

    Keyword arguments:
    id -- id of the meal to get
    Return: meal with the given id
    """

    print("get meal")
    if id in meals:
        return jsonify(meals[id])
    else:
        return jsonify({"error": "no meal found"})

# get all reviews for a specific meal


@api.route('/meals/<int:id>/reviews', methods=['GET'])
def get_reviews(id):
    """Get all reviews for a specific meal

    Keyword arguments:
    id -- id of the meal to get the reviews for
    Return: list of reviews for the meal with the given id
    """

    if id in reviews:
        return jsonify(reviews[id])
    else:
        return jsonify([])


if __name__ == '__main__':
    print("server ready")
    api.run(debug=True)
