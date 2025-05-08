from tkinter import *
from tkinter import font
from Classes import *

Drinks = Dish("Drinks")
Desserts = Dish("Desserts")
Appetizers = Dish("Appetizers")

Default_dish_list = [Appetizers, Drinks, Desserts]
Dish_list = []

def add_new(dish_name):
    new_dish = Dish(dish_name)
    Dish_list.append(new_dish)

def open_tab():
    dish_catalogue = Tk()
    lbl = Label(dish_catalogue, text="Add from preset:", anchor="center", width=20, height=4, font=("PT Sans", 14, "bold"))

    dish_catalogue.title("Add new")
    dish_catalogue.geometry('400x400')
        
    lbl.grid()
    
    existing_names = [dish.name for dish in Dish_list]

    for i in Default_dish_list:
        if i.name not in existing_names:
            i.make_button(window=dish_catalogue, foo=add_new(i.name))

    dish_catalogue.mainloop()


# instance of a Tk class
Menu = Tk()

# window config
Menu.title("Menu")
Menu.geometry('1400x400')                        # win resolution
#print(font.families())
lbl = Label(Menu, text="No dishes added yet.", 
            width=20, height=4, anchor="center", font=("PT Sans", 14, "bold"))  # first label

if len(Dish_list) == 0:
    lbl.grid()
    btn = Button(Menu, text="Add new dish...", anchor="center", command=open_tab)
    btn.grid()
else:
    pass

Menu.mainloop()                                 # execute tkinter

print(Dish_list)
