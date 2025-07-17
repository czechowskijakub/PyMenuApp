from tkinter import *
from CustomDish import *

class PositionsWindow:
    def __init__(self, parent, dish_manager, bill_manager, dish):
        self.parent = parent
        self.dish_manager = dish_manager
        self.bill_manager = bill_manager
        self.dish = dish
    
        self.dish_tab = Toplevel(parent)
        self.dish_tab.title(dish.name)

        self.display()
            
    def add_position(self, event=None):
        name = str(self.name_entry.get()).capitalize()
        price = self.price_entry.get()
        
        if name and price:
            try:
                price = float(price)
            except ValueError:
                print("Has to be a number.")
        
        if name in self.dish.Positions_list:
            print("Position already exists.")
        
        self.dish.Positions_list[name] = price
        self.name_entry.delete(0, END)
        self.price_entry.delete(0, END)
        
        self.update()
            
    def update(self):
        for widget in self.dish_tab.winfo_children():
            widget.destroy()      

        self.display()
        
    def display(self):
        lbl = Label(self.dish_tab, 
            text = f"{self.dish.name} Positions:", 
            anchor = "center",
            width = 30,
            height = 2,
            font = ("PT Sans", 14, "bold")
        )
        lbl.grid()
    
        for pos, price in self.dish.Positions_list.items():
            dish_btn = Button(self.dish_tab, 
                    text = f"{pos}: {price}zl", 
                    command = lambda p=pos, pr=price: self.bill_manager.add_position(p, pr)
            )               
            dish_btn.grid(padx=5, pady=2)
            
        self.name_entry = Entry(self.dish_tab, width=10)
        self.name_entry.grid(pady=5)
        self.price_entry = Entry(self.dish_tab, width=10)
        self.price_entry.grid(pady=5)
        
        self.accept_btn = Button(self.dish_tab, text="Add position", command=self.add_position)
        self.accept_btn.grid()
        
        self.price_entry.bind("<Return>", self.add_position)
    
    def remove_position(self):
        pass
        