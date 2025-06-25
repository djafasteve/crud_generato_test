from fastapi import FastAPI, HTTPException
from . import storage
from .schemas import Recipe, RecipeCreate

app = FastAPI(title="Recipe API")


@app.post("/recipes", response_model=Recipe, status_code=201)
def create_recipe(recipe: RecipeCreate):
    return storage.add_recipe(recipe)


@app.get("/recipes", response_model=list[Recipe])
def read_recipes():
    return storage.list_recipes()


@app.delete("/recipes/{recipe_id}", status_code=204)
def remove_recipe(recipe_id: int):
    success = storage.delete_recipe(recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return None
