# Functions that create the files used by Meal Tracker. Can be ran standalone to

from new_or_existing_user import get_user_name
from new_or_existing_user import check_if_existing


def create_meal_tracker(name):
    """
    Create a meal tracker file for a user if it does not already exist.

    Parameters:
    name (str): The name of the user for whom to create the meal tracker.

    The function checks if a meal tracker file for the given user already exists.
    If not, it creates a new text file with sections for Breakfast, Lunch, Dinner, and Snacks.
    """
    file_exists = check_if_existing(name)
    if not file_exists:
        file_name = name + ".txt"
        with open(file_name, "w") as file:
            file.write(
                "Breakfast: \nLunch: \nDinner: \nSnacks: \n")
            file.close()
    else:
        pass


def create_account_tracker():
    """
    Create an account tracker file if it does not already exist.

    The function attempts to create a new file named 'Accounts.txt'.
    If the file already exists, the function does nothing.
    The file contains a header 'Current Users:' to list user accounts.
    """
    try:
        with open("Accounts.txt", "x") as file:
            file.write("Current Users: \n")
    except:
        pass


def create_new_files(name):
    """
    Create new account and meal tracker files for a new user.

    Parameters:
    name (str): The name of the user for whom to create the account and meal tracker.

    The function calls create_account_tracker() to create an account tracker file if needed,
    and then calls create_meal_tracker() to create a meal tracker file for the user.
    """
    create_account_tracker()
    create_meal_tracker(name)
