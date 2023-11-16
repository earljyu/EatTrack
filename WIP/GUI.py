from tkinter import *


def gui():
    # creates the main window
    meal_window = Tk()

    # root window title and dimension
    meal_window.title("Meal Tracker")
    # Set geometry (widthxheight)
    meal_window.geometry('300x600')

    lbl = Label(meal_window,
                text=f"Hello, ! This is a simple meal tracker, developed by Earl Yu.")
    lbl.grid()

    name_input = Entry(meal_window, width=20,)
    name_input.grid(column=1, row=0)

    #

    def clicked():
        lbl.configure(text="Enter ")

    btn = Button(meal_window, text="Click me",
                 fg="red", command=clicked)
    # set Button grid
    btn.grid(column=1, row=0)

    # all widgets will be here
    # Execute Tkinter
    meal_window.mainloop()
