from tkinter import *
from tkinter import font
from Classes import *

Drinks = Dish("Drinks")
Drinks.add_dish_position("Cappucino", 12)
Drinks.add_dish_position("Cafe Latte", 16)

Desserts = Dish("Desserts")
#Desserts.add_dish_position("cake")

Appetizers = Dish("Appetizers")

Default_dish_list = [Appetizers, Drinks, Desserts]
Dish_list = []

def add_new(dish):
    if dish not in Dish_list:
        Dish_list.append(dish)
        update_main_menu()

def on_dish_add(dish):
    add_new(dish)

def open_dish_tab(dish):
    dish_tab = Toplevel()
    dish_tab.title(dish.name)
    lbl = Label(dish_tab, text=f"{dish.name} Positions:", anchor="center", width=30, height=2, font=("PT Sans", 14, "bold"))
    lbl.grid()

    for pos, price in dish.Positions_list.items():
        dish_btn = Button(dish_tab, text=f"{pos} - {price}zl")
        dish_btn.grid(padx=5, pady=2)


def open_tab():
    dish_catalogue = Toplevel()
    lbl = Label(dish_catalogue, text="Add from preset:", anchor="center", width=20, height=4, font=("PT Sans", 14, "bold"))
    dish_catalogue.title("Add new")
    dish_catalogue.geometry('400x400')
    lbl.grid()

    existing_names = [d.name for d in Dish_list]

    for i in Default_dish_list:
        if i.name not in existing_names:
            i.make_button(window=dish_catalogue, foo=lambda i=i: on_dish_add(i))

def update_main_menu():
    for widget in Menu.winfo_children():
        widget.destroy()

    if len(Dish_list) == 0:
        lbl = Label(Menu, text="No dishes added yet.", width=20, height=4, anchor="center", font=("PT Sans", 14, "bold"))
        lbl.grid()
    else:
        for dish in Dish_list:
            dish_btn = Button(Menu, text=dish.name, font=("PT Sans", 12), width=20, command=lambda d=dish: open_dish_tab(d))
            dish_btn.grid(padx=5, pady=5)

    btn = Button(Menu, text="Add new dish...", command=open_tab)
    btn.grid(pady=10)

# Main Menu
Menu = Tk()
Menu.title("Menu")
Menu.geometry('400x400')

update_main_menu()
Menu.mainloop()