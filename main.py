# This program will track what you ate.

from create_files import *
from new_or_existing_user import *
from meal_input import *

if __name__ == "__main__":
    name = get_user_name()
    create_new_files(name)
    create_account(name)
    meals_input()