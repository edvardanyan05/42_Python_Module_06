def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.lower()
    lst = ["earth", "air", "fire", "water"]
    for elem in lst:
        if elem.lower() in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
