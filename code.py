from heapq_max import *
from dateutil.relativedelta import relativedelta
import datetime

r = open("recipes.txt")
i = open("ingredients.txt")

recipes1 = []
ingredients = []

for line in r:
    key = line[:-1]
    key = key.lower()
    recipes1.append(key)

for line1 in i:
    line1 = line1[:-1]
    val = list(line1.split(","))
    ingredients.append(val)

recipes_ingredients = dict(zip(recipes1, ingredients))


def addProduct():
    ingredients_exp = {}

    while True:
        product = input("What product would you like to add? (To quit press <Enter>): ").lower()
        if product == "":
            break
        today = datetime.date.today()
        print("Today's date:", today)

        date_entry = input('What is the expiration date? (Enter a date in YYYY-MM-DD format): ')
        year, month, day = map(int, date_entry.split('-'))

        exp_date = datetime.datetime(year, month, day)

        time_difference = relativedelta(exp_date, today)
        difference_years = time_difference.years
        difference_months = time_difference.months
        difference_days = time_difference.days

        print("Your product will expire in:", difference_years, "years,", difference_months, "months and",
              difference_days, "days.")

        years_to_days = difference_years * 365
        months_to_days = difference_months * 30
        difference_total_days = difference_days + years_to_days + months_to_days

        ingredients_exp[product] = difference_total_days

    return ingredients_exp


def recipes_list(recipes, a):
    ingredient_list = recipes_ingredients[a.lower()]
    return ingredient_list


def dishes(recipes_ingredients1, food_in_fridge):
    values_heap = []
    food_list = [*food_in_fridge]
    food_list = set(food_list)

    for recipe, ingredients2 in recipes_ingredients1.items():
        items = set(ingredients2)
        x = len(food_list & items)
        heapq_max.heappush_max(values_heap, (x, recipe))
    while True:
        print("\nYou can cook these three meals: ")
        chosenRecipe = heappop_max(values_heap)
        print("\n", chosenRecipe[1], recipes_ingredients1[chosenRecipe[1]])
        chosenRecipe = heappop_max(values_heap)
        print("\n", chosenRecipe[1], recipes_ingredients1[chosenRecipe[1]])
        chosenRecipe = heappop_max(values_heap)
        print("\n", chosenRecipe[1], recipes_ingredients1[chosenRecipe[1]])
        answer = input("\nWould you like to see more recipes? (press <enter> to see more recipes): ")
        if answer == "":
            continue
        else:
            break


def main():
    answer = input(
        "Would you like to look for a recipe (r), cook something with the ingredients you have (c) or press (q) to quit: ")
    if answer == "r":
        print("Here is a list of all possible meals:")
        print([*recipes_ingredients])
        user_recipe = input("What meal would you like to know more about?: ")
        print(recipes_list(recipes1, user_recipe))

    elif answer == "c":
        food_in_fridge = addProduct()
        dishes(recipes_ingredients, food_in_fridge)

    elif answer == "q":
        print("Thank you for using Fridge Friends")

    else:
        print("Please type a valid response:")
        main()


if __name__ == "__main__":
    main()
