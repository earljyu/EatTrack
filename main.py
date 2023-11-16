# This program will track what you ate.

from create_files import *
from new_or_existing_user import *
from meal_input import *
# from tkinter import *
# from GUI import *

if __name__ == "__main__":

    # keep_going = True

    # while keep_going == True:

    name = get_user_name().capitalize()
    create_new_files(name)
    create_account(name)
    meal_input(name)

    # while True:
    #     response = input(
    #         "Would someone else like to enter data? (Y/N)").lower()
    #     if response == "y":
    #         break
    #     elif response == "n":
    #         keep_going = False
    #         break
    #     else:
    #         print("""Please response with "Y" or "N"!""")
