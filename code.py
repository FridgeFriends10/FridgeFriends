from heapq_max import *
from dateutil.relativedelta import relativedelta
import datetime
import webbrowser
import time
from pywebio.input import *
from pywebio.output import *

put_markdown("WELCOME TO FRIDGE FRIENDS®", scope="ROOT")
with put_loading():

    put_text("Please make sure you don't have already uploaded the files, if you have please delete them from your code editor but not from your computer")
    put_text("Now the program will ask for a file to import, please choose recipes.txt")
    time.sleep(3)
    put_text("In 3 seconds")
    time.sleep(1)
    put_text("In 2 seconds")
    time.sleep(1)
    put_text("In 1 second")
    time.sleep(1)
recipes_file = file_upload("Select recipes.txt")

with put_loading():

    put_text("Now the program will ask for another file to import, please choose ingredients.txt")
    time.sleep(3)
    put_text("In 3 seconds")
    time.sleep(1)
    put_text("In 2 seconds")
    time.sleep(1)
    put_text("In 1 second")
    time.sleep(1)
ingredients_file = file_upload("Select ingredients.txt")

recipes_file = recipes_file["content"]
recipes_file = recipes_file.decode("utf-8")
with open("recipes.txt", "a") as recipes_file1:
    recipes_file1.write(recipes_file)

ingredients_file = ingredients_file["content"]
ingredients_file = ingredients_file.decode("utf-8")
with open("ingredients.txt", "a") as ingredients_file1:
    ingredients_file1.write(ingredients_file)


recipes1 = []
ingredients = []
r = open("recipes.txt")
i = open("ingredients.txt")
for line in r:
    key = line[:-1]
    key = key.lower()
    recipes1.append(key)

for line1 in i:
    line1 = line1[:-1]
    val = list(line1.split(","))
    ingredients.append(val)


recipes_ingredients = dict(zip(recipes1, ingredients))



def register():
    userName = input(placeholder="Username")
    passWord = input(placeholder="Password", type=PASSWORD)
    with open("accounts.txt", "a") as f:
        f.write(userName + "|" + passWord + "|")


def login():
    global userName
    global passWord

    list = []
    infile = open("accounts.txt", "r")
    line = infile.readline()
    while line != "":

        for word in line.split("|"):
            list.append(word)
        line = infile.readline()
    list.pop(-1)
    dictionary = {}
    x = len(list)
    y = int(x / 2)
    for i in range(len(list) - y):
        dictionary[list[i]] = list[i + 1]
        list.pop(0)
    userName = input(placeholder="Username")
    passWord = input(placeholder="Password", type=PASSWORD)
    x = dictionary.get(userName)

    if passWord == x:
        put_text("Welcome back,", userName)
    else:
        toast("Username and Password or not correct")
        put_text("The username or password is incorrect, please try again")
        login()


def addProduct():
    products = input('Enter elements of a list separated by a comma ').lower()
    user_list = products.split(",")
    put_text('list: ', user_list)
    return products


def addDate(products):
    ingredients_exp = {}
    today = datetime.date.today()
    put_text("Today's date:", today)
    for x in range(len(products)):
        date_entry = input('What is the expiration date? (Enter a date in YYYY-MM-DD format): ')
        year, month, day = map(int, date_entry.split('-'))

        exp_date = datetime.datetime(year, month, day)

        time_difference = relativedelta(exp_date, today)
        difference_years = time_difference.years
        difference_months = time_difference.months
        difference_days = time_difference.days

        put_text("Your product will expire in:", difference_years, "years,", difference_months, "months and",
                 difference_days, "days.")

        years_to_days = difference_years * 365
        months_to_days = difference_months * 30
        difference_total_days = difference_days + years_to_days + months_to_days
        ingredients_exp[x] = difference_total_days

    return ingredients_exp


def recipes_list(recipes, a):
    ingredient_list = recipes_ingredients[a.lower()]
    return ingredient_list


def dishes(recipes_ingredients1, food_in_fridge):
    values_heap = []
    products = food_in_fridge
    food_in_fridge = set(food_in_fridge)

    for recipe, ingredients2 in recipes_ingredients1.items():
        items = set(ingredients2)
        x = len(food_in_fridge & items)
        heapq_max.heappush_max(values_heap, (x, recipe))
    while True:
        put_text("\nYou can cook these three meals: ")
        chosenRecipe = heappop_max(values_heap)
        put_text("\n", chosenRecipe[1], recipes_ingredients1[chosenRecipe[1]])
        chosenRecipe = heappop_max(values_heap)
        put_text("\n", chosenRecipe[1], recipes_ingredients1[chosenRecipe[1]])
        chosenRecipe = heappop_max(values_heap)
        put_text("\n", chosenRecipe[1], recipes_ingredients1[chosenRecipe[1]])
        answer = select("WHat would you like to do?", ["See more recipes", "Buy the missing products", "Watch how to cook the dish on YouTube"])
        if answer == "See more recipes":
            continue
        if answer == "Watch how to cook the dish on YouTube":
            video = input("What is the name of the receipe you chose?:")
            c = "https://www.youtube.com/results?search_query="
            webbrowser.open(c + video, new=0)
            put_text("\nThank you for using Fridge Friends®")
            put_text(
                "\nIf you liked the program please share it in your social media: https://github.com/FridgeFriends10/FridgeFriends")
            put_text("\nAny problem or recommendation to improve the program please contact.")
            put_text("\nEmail: FridgeFriends10@gmail.com")
            put_text(
                "\nProject created and developed by: \nLucia Gil \nVirginia Levi \nAlba San Cristóbal \nMartin Mir \nJaime Echevarría \nJuan Peláez ")
            break
        if answer == "Buy the missing products":
            ingredients_missing(products)
            answer2 = select("Would you like to use FridgeFriends again?", ["Yes", "No"])
            if answer2 == "Yes":
                main()
            if answer2 == "No":
                put_text("\nThank you for using Fridge Friends®")
                put_text(
                    "\nIf you liked the program please share it in your social media: https://github.com/FridgeFriends10/FridgeFriends")
                put_text("\nAny problem or recommendation to improve the program please contact.")
                put_text("\nEmail: FridgeFriends10@gmail.com")
                put_text(
                    "\nProject created and developed by: \nLucia Gil \nVirginia Levi \nAlba San Cristóbal \nMartin Mir \nJaime Echevarría \nJuan Peláez ")
                quit()


def nutrition():
    answer = input("\nWhat dish would you like to know the nutritious information about?: ")
    v = "https://www.nutritionvalue.org/search.php?food_query="
    webbrowser.open(v + answer, new=0)
    put_text("\nThank you for using Fridge Friends®")
    put_text(
        "\nIf you liked the program please share it in your social media: https://github.com/FridgeFriends10/FridgeFriends")
    put_text("\nAny problem or recommendation to improve the program please contact the team.")
    put_text("\nEmail: FridgeFriends10@gmail.com")
    put_text(
        "\nProject created and developed by: \nLucia Gil \nVirginia Levi \nAlba San Cristóbal \nMartin Mir \n Jaime Echevarría \n Juan Peláez ")
    quit()


def ingredients_missing(products):
    user_recipe1 = input("What dish recipe have you chosen?: ")
    ingredients2 = recipes_list(recipes1, user_recipe1)
    products = products.split(",")
    a = list(set(ingredients2) - set(products))
    for x in a:
        put_text("You are missing this ingredient:", x)
        x = x.replace(" ", "")
        m = "https://www.walmart.com/search?q="+x
        put_link("Click here for:"+x, url=m)


def main():
    put_markdown("WELCOME TO FRIDGE FRIENDS")
    option1 = select("Are you new? Or do you have an existing account?", ["Register", "Login"])
    if option1 == "Register":
        register()
    if option1 == "Login":
        login()
    toast("Login Successful")
    put_text("\nWelcome to Fridge Friends", userName)
    options2 = select("What would you like to do?",["Look for a recipe", "Search for nutritional fact", "Cook a dish with ingredients you have"])

    if options2 == "Look for a recipe":
        put_text("Here is a list of all possible meals:")
        put_scrollable([*recipes_ingredients])
        user_recipe = input("\nWhat meal would you like to know more about?: ")
        ingredients1 = recipes_list(recipes1, user_recipe)
        put_text("\nThese are the ingredients you need for that dish:", ingredients1)

    elif options2 == "Search for nutritional fact":
        nutrition()

    elif options2 == "Cook a dish with ingredients you have":
        food_in_fridge = addProduct()
        dishes(recipes_ingredients, food_in_fridge)


if __name__ == "__main__":
    main()
