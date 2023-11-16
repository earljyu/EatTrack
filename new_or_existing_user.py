# This file checks of the name entered in get_user_name already has data associated with it. If not, it will store the name as a new value.

def get_user_name():
    """
    Prompt the user to enter their first name and return it.

    Returns:
    str: The first name entered by the user.

    This function asks the user to input their first name and returns the entered name as a string.
    """
    user_name = input("What is your first name: ")
    return user_name


def check_if_existing(name):
    """
    Check if a given name exists in the 'Accounts.txt' file.

    Parameters:
    name (str): The name to check in the account file.

    Returns:
    bool: True if the name exists in the file, False otherwise.

    This function reads the 'Accounts.txt' file and checks if the given name is present.
    It compares the name case-insensitively and returns a boolean value indicating the presence of the name.
    """
    name = name.capitalize()
    with open("Accounts.txt", 'r') as file:
        lines = file.readlines()
        existing_check = False
        for line in lines:
            line = line.rstrip("\n")
            if (name in line) or (name.casefold() == line.casefold()):
                return True
                break
        else:
            return False


def create_account(name):
    """
    Create a new account or welcome back an existing user based on the given name.

    Parameters:
    name (str): The name of the user to create an account for or to check for existing account.

    This function checks if an account with the given name already exists in 'Accounts.txt'.
    If the account exists, it welcomes back the user. If not, it creates a new account by appending the name to the file.
    """
    check = check_if_existing(name)
    if check == True:
        print(f"\n\n{name.capitalize()}, welcome back.\n\n")
    else:
        with open("Accounts.txt", 'a') as account_file:
            name = name.capitalize()
            account_file.write(f"{name}\n")
            print(f"\n\nHello {name}, Welcome. \n\n")


# def account_selector():

# Old create_account() code
#
# def create_account(name):
#     with open("Accounts.txt", 'r') as file:
#         lines = file.readlines()
#         existing_user = False
#         for line in lines:
#             line = line.rstrip("\n")
#             if (name in line) or (name.casefold() == line.casefold()):
#                 print(f"{name.capitalize()}, you already have an account!")
#                 existing_user = True
#                 break

#         else:
#             with open("Accounts.txt", 'a') as account_file:
#                 account_file.write(f"{name.capitalize()}\n")
