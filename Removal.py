from tkinter import * 

class AddRemovalWindow:
    def __init__(self, parent, dish_manager, update):
        self.dish_manager = dish_manager
        self.update = update
        self.dish_buttons = {}
        
        self.window = Toplevel(parent)
        self.window.title("Remove")
        self.window.geometry("300x200")
        
        for dish in self.dish_manager.dish_list:
            btn = Button(self.window, text=dish.name, command=lambda i=dish: self.remove_dish(i))
            btn.grid()
            self.dish_buttons[dish] = btn
            self.update()
            
    def remove_dish(self, dish):
        self.dish_manager.dish_list.remove(dish)
        self.dish_buttons[dish].destroy()
        del self.dish_buttons[dish]
        self.update()