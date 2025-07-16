from tkinter import *
from App import *
from Dish import * 
from DishOptions import *
from Bill import *

if __name__ == "__main__":
    dish_manager = DishOptions("saved_profile.txt")
    bill = BillManager("bill.txt")
    
    dish_manager.load_profile()
    
    root = Tk()
    root.title("Menu")
    root.geometry("400x400")
    
    app = App(root, dish_manager, bill)
    
    root.mainloop()
    
    dish_manager.save_profile()
    bill.save_bill()
    dish_manager.load_profile()
    
    