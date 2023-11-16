***WIP***

This is a Python project that I created using concepts that I've learned in my Programming Fundamentals 1 class.

It creates a .txt file, and collects the user's input for the food they ate for breakfast, lunch, dinner, and snacks.

First Version Update (11/16/23):

 - Added docstrings to each function for readability.

 - Completed the meal_input.py module
    - meal_input.py contains meal_input(), item_input(), and file_update(). See docstrings for details.

 - Edited the new_or_existing_user.py module.
    - Changed the input prompt for get_user_name() for specificity.
    - Split create_account() into two separate functions: 
       - Added check_if_existing(), which takes the user's name as input, accesses and processes Accounts.txt, and returns whether the account exists.
       - The new create_account() passes the user's name to check_if_existing().
         - If check_if_existing() returns True, the user is greeted with "Welcome Back".
         - If check_if_existing() returns False, their name is appended to the file.

 - Edited the create_files.py module
    - The existing code is now nested within an if statement. It runs if check_if_existing() returns False. If it returns True, the function is skipped.    

 - Added WIP directory
    - For modules that will be implemented in the future, or being experimented with.