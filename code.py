from heapq_max import *
from dateutil.relativedelta import relativedelta
import datetime
import webbrowser
from tkinter.filedialog import askopenfile
import time


print("The program will ask for a file to import, please choose recipes.txt")
time.sleep(5)
print("In 3 seconds")
time.sleep(1)
print("In 2 seconds")
time.sleep(1)
print("In 1 second")
time.sleep(1)
recipes_file = askopenfile(mode='r')

print("The program will ask for another file to import, please choose ingredients.txt")
time.sleep(5)
print("In 3 seconds")
time.sleep(1)
print("In 2 seconds")
time.sleep(1)
print("In 1 second")
time.sleep(1)
ingredients_file = askopenfile(mode='r')


recipes1 = []
ingredients = []

for line in recipes_file:
    key = line[:-1]
    key = key.lower()
    recipes1.append(key)

for line1 in ingredients_file:
    line1 = line1[:-1]
    val = list(line1.split(","))
    ingredients.append(val)

recipes_ingredients = dict(zip(recipes1, ingredients))


def register():
    global userName
    global passWord
    userName = input("\nUser Name: ")
    passWord = input("\nPassword: ")

    with open("accounts.txt", "a") as f:
        f.write(userName + "|" + passWord + "|")


def login():
    global userName
    global passWord
    userName = input("\nUser Name: ")
    passWord = input("\nPassword: ")
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

    x = dictionary.get(userName)
    if passWord == x:
        print("\nWelcome back,", userName)
    else:
        print("\nThe username or password is incorrect, please try again")
        quit()


def addProduct():
    products = input('Enter elements of a list separated by a comma ').lower()
    user_list = products.split(",")
    print('list: ', user_list)
    return products


def addDate(products):
    ingredients_exp = {}
    today = datetime.date.today()
    print("Today's date:", today)
    for x in range(len(products)):
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
        print("\nYou can cook these three meals: ")
        chosenRecipe = heappop_max(values_heap)
        print("\n", chosenRecipe[1], recipes_ingredients1[chosenRecipe[1]])
        chosenRecipe = heappop_max(values_heap)
        print("\n", chosenRecipe[1], recipes_ingredients1[chosenRecipe[1]])
        chosenRecipe = heappop_max(values_heap)
        print("\n", chosenRecipe[1], recipes_ingredients1[chosenRecipe[1]])
        print("\nWould you like to see more recipes? (press <enter> to see more recipes),")
        answer = input("watch how to do the recipe on YT (press w), buy the missing products (b) or quit(q): ")
        if answer == "":
            continue
        if answer == "w":
            video = input("What is the name of the receipe you chose?:")
            c = "https://www.youtube.com/results?search_query="
            webbrowser.open(c + video, new=0)
            print("\nThank you for using Fridge Friends®")
            print("\nIf you liked the program please share it in your social media: https://github.com/FridgeFriends10/FridgeFriends")
            print("\nAny problem or recommendation to improve the program please contact.")
            print("\nEmail: FridgeFriends10@gmail.com")
            print("\nProject created and developed by: \nLucia Gil \nVirginia Levi \nAlba San Cristóbal \nMartin Mir \nJaime Echevarría \nJuan Peláez ")
            break
        if answer == "b":
            ingredients_missing(products)
            answer2 = input("Would you like to use FridgeFriends again? (yes or no): ").lower()
            if answer2 == "yes":
                main()
            else:
                print("\nThank you for using Fridge Friends®")
                print(
                    "\nIf you liked the program please share it in your social media: https://github.com/FridgeFriends10/FridgeFriends")
                print("\nAny problem or recommendation to improve the program please contact.")
                print("\nEmail: FridgeFriends10@gmail.com")
                print(
                    "\nProject created and developed by: \nLucia Gil \nVirginia Levi \nAlba San Cristóbal \nMartin Mir \nJaime Echevarría \nJuan Peláez ")
                quit()
        else:
            print("\nThank you for using Fridge Friends®")
            print(
                "\nIf you liked the program please share it in your social media: https://github.com/FridgeFriends10/FridgeFriends")
            print("\nAny problem or recommendation to improve the program please contact the team.")
            print("\nEmail: FridgeFriends10@gmail.com")
            print(
                "\nProject created and developed by: \nLucia Gil \nVirginia Levi \nAlba San Cristóbal \nMartin Mir \nJaime Echevarría \nJuan Peláez ")
            break


def nutrition():
    answer = input("\nWhat dish would you like to know the nutritious information about?: ")
    v = "https://www.nutritionvalue.org/search.php?food_query="
    webbrowser.open(v + answer, new=0)
    print("\nThank you for using Fridge Friends®")
    print(
        "\nIf you liked the program please share it in your social media: https://github.com/FridgeFriends10/FridgeFriends")
    print("\nAny problem or recommendation to improve the program please contact the team.")
    print("\nEmail: FridgeFriends10@gmail.com")
    print(
        "\nProject created and developed by: \nLucia Gil \nVirginia Levi \nAlba San Cristóbal \nMartin Mir \n Jaime Echevarría \n Juan Peláez ")
    quit()


def ingredients_missing(products):
    user_recipe1 = input("What dish recipe have you chosen?: ")
    ingredients2 = recipes_list(recipes1, user_recipe1)
    products = products.split(",")
    a = list(set(ingredients2)-set(products))
    for x in a:
        print("You are missing this ingredient:", x)
        x = x.replace(" ","")
        m = "https://www.walmart.com/search?q="
        print(m+x)


def main():
    answer0 = input("\nHi there!, would you like to register or login to an existing account?: ").lower()

    if answer0 == "register":
        register()

    elif answer0 == "login":
        login()

    elif answer0 == "":
        quit()

    else:
        print("Please choose to register or to login (register, login).")
        main()

    print("\nWelcome to Fridge Friends", userName)
    print("\nWould you like to look for a recipe (r), search for nutritional facts of a dish (n)")
    answer = input("cook something with the ingredients you have (c) or press (q) to quit: ")

    if answer == "r":
        print("Here is a list of all possible meals:")
        print([*recipes_ingredients])
        user_recipe = input("\nWhat meal would you like to know more about?: ")
        ingredients1 = recipes_list(recipes1, user_recipe)
        print("\nThese are the ingredients you need for that dish:", ingredients1)

    elif answer == "n":
        nutrition()

    elif answer == "c":
        food_in_fridge = addProduct()
        dishes(recipes_ingredients, food_in_fridge)

    elif answer == "q":
        print("\nThank you for using Fridge Friends®")
        print(
            "\nIf you liked the program please share it in your social media: https://github.com/FridgeFriends10/FridgeFriends")
        print("\nAny problem or recommendation to improve the program please contact the team.")
        print("\nEmail: FridgeFriends10@gmail.com")
        print(
            "\nProject created and developed by: \nLucia Gil \nVirginia Levi \nAlba San Cristóbal \nMartin Mir \nJaime Echevarría \nJuan Peláez ")
        quit()

    else:
        print("Please type a valid response:")
        main()


if __name__ == "__main__":
    main()
