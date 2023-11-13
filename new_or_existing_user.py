# This file checks of the name entered in get_user_name already has data associated with it. If not, it will store the name as a new value.

def get_user_name():
    user_name = input("What is your name: ")
    return user_name


def create_account(name):
    with open("Accounts.txt", 'r') as file:
        lines = file.readlines()
        found = False
        for line in lines:
            line = line.rstrip("\n")
            if (name in line) or (name.casefold() == line.casefold()):
                print(f"{name}, you already have an account!")
                break

        else:
            with open("Accounts.txt", 'a') as account_file:
                account_file.write(f"{name}\n")


# def account_selector():
