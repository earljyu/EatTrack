# Functions that create the files used by Meal Tracker. Can be ran standalone to

from new_or_existing_user import get_user_name


def create_meal_tracker(name):
    file_name = name + ".txt"
    with open(file_name, "w") as file:
        file.write("Breakfast:\nLunch:\nDinner:\nSnacks:")
        file.close()


def create_account_tracker():
    try:
        with open("Accounts.txt", "x") as file:
            file.write("Current Users\n")
    except:
        pass


def create_new_files(name):
    create_meal_tracker(name)
    create_account_tracker()
