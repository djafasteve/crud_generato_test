import json
from pathlib import Path
from typing import List

from .schemas import Recipe, RecipeCreate

DATA_FILE = Path("recipes.json")


def _load_data() -> List[dict]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def _save_data(recipes: List[dict]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(recipes, f, indent=2)


def list_recipes() -> List[Recipe]:
    return [Recipe(**r) for r in _load_data()]


def add_recipe(recipe_in: RecipeCreate) -> Recipe:
    recipes = _load_data()
    next_id = max((r["id"] for r in recipes), default=0) + 1
    recipe_data = recipe_in.dict()
    recipe_data["id"] = next_id
    recipes.append(recipe_data)
    _save_data(recipes)
    return Recipe(**recipe_data)


def delete_recipe(recipe_id: int) -> bool:
    recipes = _load_data()
    new_recipes = [r for r in recipes if r["id"] != recipe_id]
    if len(new_recipes) == len(recipes):
        return False
    _save_data(new_recipes)
    return True
