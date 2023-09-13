
from recipefinder import main
import pytest

def test_main():
    ingredient = "cream of tarter"
    recipe = main(ingredient)

    # Verify that the main function returned a recipe.
    assert isinstance(recipe), \
        f"main function returned a recipe containing {ingredient}"

    # Verify that the main function returned the correct value.
    assert recipe == "Snickerdoodles\
3/4 C. sugar\
1/2 C. butter\
1 egg\
1/2 tsp. vanilla\
1 1/2 C. flour\
1/4 tsp. salt\
4 tsp. baking soda\
1/4 tsp. cream of tarter\
2 TBSP sugar\
2 tsp. cinnamon\
In a large bowl mix cream sugar and butter, add eggs and vanilla. In a small bowl add flour, salt, baking soda and cream of tarter. Add to the butter mixture and mix well. In a small dish mix sugar and cinnamon together. Make small balls and roll into cinnamon/sugar mixture. Place on baking sheet. Bake 375 for 8 min."

def test_ingredient_match():
    ingredient = "apple"
    recipe = main(ingredient)

    # Verify that the main function returned a recipe.
    assert isinstance(recipe), \
        f"main function returned a recipe containing {ingredient}"

    # Verify that the main function returned the correct value.
    assert recipe == f"There are no recipes containing "{ingredient}" please try again!"


pytest.main(["-v", "--tb=line", "-rN", __file__])
