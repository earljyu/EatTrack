from new_or_existing_user import *


def meal_input(name):
    """
    Process meal entries for a specified user.

    Parameters:
    name (str): The name of the user.

    Reads the user's meal file and calls item_input for each meal type (Breakfast, Lunch, Dinner, Snacks).
    Each call to item_input updates the line number for subsequent entries.
    """
    file_name = name.capitalize() + ".txt"
    with open(file_name, "r") as file:
        lines = file.readlines()
        meal_being_input = ""
        line_num = 1
        for line in lines:
            if "Breakfast:" in line:
                meal_being_input = "Breakfast"
                line_num = item_input(
                    file_name, meal_being_input, line_num, False)
            if "Lunch:" in line:
                meal_being_input = "Lunch"
                line_num = item_input(
                    file_name, meal_being_input, line_num + 1, False)
            if "Dinner:" in line:
                meal_being_input = "Dinner"
                line_num = item_input(
                    file_name, meal_being_input, line_num + 1, False)
            if "Snacks:" in line:
                meal_being_input = "Snacks"
                line_num = item_input(
                    file_name, meal_being_input, line_num + 1, True)


def item_input(account_file, meal, line, is_last_meal):
    """
    Handle the input of food items for a specific meal.

    Parameters:
    account_file (str): The file name of the user's meal account.
    meal (str): The type of meal (e.g., Breakfast, Lunch, Dinner, Snacks).
    line (int): The line number in the file to start the input.
    is_last_meal (bool): Flag to indicate if this is the last meal entry.

    Prompts the user to enter food items for the specified meal.
    Updates the file with the entered items and prints appropriate messages based on user input and whether it's the last meal.
    Returns the line number where the last item was added.
    """
    current_line = line
    while True:
        initial_response = input(
            f"Would you like to enter the food items for {meal}? (Y/N)")
        if initial_response.lower() == "y":
            file_update(account_file, meal, line)
            current_line += 1
            while True:
                response = input(
                    "Would you like to add another food item? (Y/N)")
                if response.lower() == "y":
                    file_update(account_file, meal, current_line)
                    current_line += 1
                elif response.lower() == "n":
                    if is_last_meal:
                        print("Thanks. Goodbye!")
                    else:
                        print("Okay, next meal!")
                    break
                else:
                    print("Your response needs to be (Y/N)")
            break
        elif initial_response.lower() == "n":
            if is_last_meal:
                print("Thanks. Goodbye!")
            else:
                print("Okay, next meal!")
            break
        else:
            print("You need to answer in the correct format. Try again.")
    return current_line


def file_update(file_name, meal, linenumber):
    """
    Update the meal file with a new food item at a specified line.

    Parameters:
    file_name (str): The file name of the user's meal account.
    meal (str): The type of meal (e.g., Breakfast, Lunch, Dinner, Snacks).
    linenumber (int): The line number in the file where the new item should be inserted.

    Prompts the user for a food item and inserts it into the file at the specified line.
    """
    new_food_item = input("What food item would you like to enter? ")
    with open(file_name, "r") as file:
        lines = file.readlines()
        lines.insert(linenumber, new_food_item+"\n")
        with open(file_name, "w") as file:
            for line in lines:
                file.write(line)

# for line in lines:
#     with open(filename, "w") as file:
#         file.write(line)


# elif "Lunch:_______" in line:
#     meal_being_input = "Lunch"

# elif "Dinner:_______" in line:
#     meal_being_input = "Dinner"

# elif "Snacks:_______" in line:
#     meal_being_input = "Snacks"


# with open(file, 'r+') as fd:
#     contents = fd.readlines()
#     contents.insert(index, new_string)  # new_string should end in a newline
#     fd.seek(0)  # readlines consumes the iterator, so we need to start over
#     fd.writelines(contents)  # No need to truncate as we are increasing filesize

#     with open(file, 'r+') as fd:
#     contents = fd.readlines()
#     if match_string in contents[-1]:  # Handle last line to prevent IndexError
#         contents.append(insert_string)
#     else:
#         for index, line in enumerate(contents):
#             if match_string in line and insert_string not in contents[index + 1]:
#                 contents.insert(index + 1, insert_string)
#                 break
#     fd.seek(0)
#     fd.writelines(contents)
# def lunch_input():
#     pass

# def dinner_input():
#     pass

# def snacks_input():
#     pass

# def meals_input():
#     breakfast_input()
#     lunch_input()
#     dinner_input()
#     snacks_input()
