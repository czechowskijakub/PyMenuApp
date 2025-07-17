from tkinter import *
from Dish import *

class AddDishWindow:
    def __init__(self, parent, dish_manager, update):
        self.dish_manager = dish_manager
        self.update = update
        
        self.window = Toplevel(parent)
        self.window.title("Add new")
        self.window.geometry("300x200")

        lbl = Label(self.window, text = "Add your dish:")
        lbl.pack(pady=10)
        self.entry = Entry(self.window)
        self.entry.pack()
        self.entry.bind("<Return>", self.add_dish)
        self.update

        btn = Button(self.window, text="OK", command=self.add_dish)
        btn.pack(pady=10)

    def add_dish(self, event=None):
        name = str(self.entry.get().capitalize())
        d_names_existing = [dish.name for dish in self.dish_manager.dish_list]
        if name.isalpha() and name not in d_names_existing:
            self.dish_manager.dish_list.append(Dish(name))
            self.entry.delete(0, END)
            self.update()
        else:
            print("Invalid or item already exists.")
