from tkinter import *
from tkinter import font
from Classes import *

global bill, saved_profile, save

# open txt files:
# bill for counting up added positions and their price
# saved_profile for saving Dish positions that you want to preserve for next boot up

bill = open("bill.txt", "w")
saved_profile = open("saved_profile.txt", "r+")

# Test examples
Drinks = Dish("Drinks")
Drinks.add_dish_position("Cappucino", 12)
Drinks.add_dish_position("Cafe Latte", 16)

Desserts = Dish("Desserts")
Desserts.add_dish_position("Frappucino", 24)

Appetizers = Dish("Appetizers")

Default_dish_list = [Appetizers, Drinks, Desserts]
Dish_list = []

count = 0

def sum_up():
    if count != 0:
        bill.write(f"Total: {count}zl")

# save your setup -> saved_profile.txt
def save_set():
    saved_profile.seek(0)
    content = saved_profile.read()
    for dish in Dish_list:
        if dish.name not in content:
            saved_profile.write(f"{dish.name},")
            for pos, price in dish.Positions_list.items():
                saved_profile.write(f"{pos},{price},")
            saved_profile.write("\n")

# load previously used menu
def load_profile():
    saved_profile.seek(0)
    for line in saved_profile:
        line = line.strip()
        if not line:
            continue
        pos_content = line.split(",")
        dish_ctgry = Dish(pos_content[0])
        for i in range(1, len(pos_content)-1, 2):
            try:
                name = pos_content[i]
                price = float(pos_content[i+1])
                dish_ctgry.add_dish_position(name, price)
            except (ValueError, IndexError):
                print(f"Blad w linii: {line}")
        Dish_list.append(dish_ctgry)
    
def write_on_bill(position, price):
    global count
    bill.write(f"{position}: {price}zl\n")
    count += price
    
# adds new dish to the list
def add_new(dish):
    if dish not in Dish_list:
        Dish_list.append(dish)
    update_main_menu()
    
# preset tab
def open_tab():
    dish_catalogue = Toplevel()
    lbl = Label(dish_catalogue, text="Add from preset:", anchor="center", width=20, height=4, font=("PT Sans", 14, "bold"))
    dish_catalogue.title("Add new")
    dish_catalogue.geometry('400x400')
    lbl.grid()

    existing_names = [d.name for d in Dish_list]

    for i in Default_dish_list:
        if i.name not in existing_names:
            i.make_button(window=dish_catalogue, foo=lambda i=i: add_new(i))
    
# tab for positions of chosen dish
def open_dish_tab(dish):
    dish_tab = Toplevel()
    dish_tab.title(dish.name)
    lbl = Label(dish_tab, text=f"{dish.name} Positions:", anchor="center", width=30, height=2, font=("PT Sans", 14, "bold"))
    lbl.grid()
    for pos, price in dish.Positions_list.items():
        dish_btn = Button(dish_tab, text=f"{pos}: {price}zl", command=lambda p=pos, pr=price: write_on_bill(p, pr))               
        dish_btn.grid(padx=5, pady=2)

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

    btn_add_new = Button(Menu, text="Add new dish...", command=open_tab)
    btn_add_new.grid(pady=10)
    
    btn_remove = Button(Menu, text="Remove", command=open_remove_dish)
    btn_remove.grid()
    
def remove_dish(name):
    Dish_list.remove(name)    
    update_main_menu()

def open_remove_dish():
    removal = Toplevel()
    removal.title("Remove")
    for dish in Dish_list:
        dish.make_button(window=removal, foo=lambda i=dish: remove_dish(i))
    

# Main Menu
load_profile()
Menu = Tk()
Menu.title("Menu")
Menu.geometry('400x400')

update_main_menu()
Menu.mainloop()
save_set()
sum_up()
bill.close()
saved_profile.close()