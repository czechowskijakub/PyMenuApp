from tkinter import *
from Dish import *
from CustomDish import *
from Removal import *
from DishPositions import *

class App:
    def __init__(self, root, dish_manager, bill_manager):
        self.root = root
        self.dish_manager = dish_manager
        self.bill_manager = bill_manager
        self.main_frame = Frame(root)
        self.main_frame.pack()
        self.update_main_menu()
        
    def update_main_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        if not self.dish_manager.dish_list:
            lbl = Label(self.main_frame, 
                text = "No dishes added yet.", 
                width = 20, 
                height = 4, 
                anchor = "center", 
                font = ("PT Sans", 14, "bold")
            )
            lbl.grid()
        else:
            for dish in self.dish_manager.dish_list:
                btn = Button(self.main_frame,
                    text=dish.name,
                    width=20,
                    command=lambda d=dish: self.open_dish_tab(d)
                )
                btn.grid()
                
        add_btn = Button(self.main_frame, text="Add your dish", command=self.open_add_tab)
        add_btn.grid()
        rmv_btn = Button(self.main_frame, text="Remove dish", command=self.open_remove_tab)
        rmv_btn.grid()
        
    def open_dish_tab(self, dish):
        PositionsWindow(self.root, self.dish_manager, self.bill_manager, dish)
    
    def open_add_tab(self):
        AddDishWindow(self.root, self.dish_manager, self.update_main_menu)
    
    def open_remove_tab(self):  
        AddRemovalWindow(self.root, self.dish_manager, self.update_main_menu)