# Trying out OOP. Do not

from create_files import *
from new_or_existing_user import *
from meal_input import *

if __name__ == '__main__':

    class Account:

        name = get_user_name().capitalize()
