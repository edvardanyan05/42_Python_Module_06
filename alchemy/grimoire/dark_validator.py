from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.lower()
    lst = dark_spell_allowed_ingredients()
    for elem in lst:
        if elem.lower() in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
