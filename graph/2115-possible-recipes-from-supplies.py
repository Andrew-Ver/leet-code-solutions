'''
    https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
'''

from collections import defaultdict


def findAllRecipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    recipes = {recipes[i]: set(ingredients[i]) for i in range(len(recipes))}
    can_make = set(supplies)
    checked = defaultdict(int)
    cannot_make = set()
    
    def what_can_be_made(r: str) -> bool:
        needed = recipes[r]
        checked[r] += 1
        if needed.issubset(can_make):
            can_make.add(r)
        elif r in cannot_make or checked[r] > 100:
            cannot_make.add(r)
        else:
            for n in needed:
                if n in recipes and n not in cannot_make:
                    what_can_be_made(n)
                    
    for _ in range(10):                    
        for r in [rec for rec in recipes if rec not in can_make]:
            what_can_be_made(r)
                
    return [recipe for recipe in recipes if recipe in can_make]


print(findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))