from tkinter import *
from Dish import *

class App:
    def __init__(self, root, dish_manager, bill_manager):
        self.root = root
        self.dish_manager = dish_manager
        self.bill_manager = bill_manager
        self.main_frame = Frame(root)
        self.main_frame.pack()
        self.dish_buttons = {}
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
        dish_tab = Toplevel()
        dish_tab.title(dish.name)
    
        lbl = Label(dish_tab, 
            text = f"{dish.name} Positions:", 
            anchor = "center",
            width = 30,
            height = 2,
            font = ("PT Sans", 14, "bold")
        )
        lbl.grid()
        
        for pos, price in dish.Positions_list.items():
            dish_btn = Button(dish_tab, 
                    text = f"{pos}: {price}zl", 
                    command = lambda p=pos, pr=price: self.bill_manager.add_position(p, pr)
            )               
            dish_btn.grid(padx=5, pady=2)
    
    def open_add_tab(self):
        dish_catalogue = Toplevel()
        dish_catalogue.title("Add new")
        dish_catalogue.geometry('400x400')

        lbl_custom = Label(
            dish_catalogue,
            text = "Add your own:",
            anchor = "center",
            width = 20,
            height = 4,
            font = ("PT Sans", 14, "bold")
        )
        lbl_custom.grid(row=0, column=0)

        user_input = Entry(dish_catalogue, 
            width = 10, 
            font = ("PT Sans", 12)
        )
        
        user_input.grid(padx=20, pady=5)

        def on_enter(event=None):
            name = str(user_input.get().capitalize())
            dnames_existing = [dish.name for dish in self.dish_manager.dish_list]
            if name not in dnames_existing and name.isalpha():
                self.dish_manager.dish_list.append(Dish(name))
                user_input.delete(0, END)
                self.update_main_menu()
            else:
                print("no.")

        user_input.bind("<Return>", on_enter)

        accept = Button(
            dish_catalogue,
            text="OK",
            anchor="center",
            command=on_enter
        )
        accept.grid(pady=10)
        user_input.focus()
    
    def open_remove_tab(self):  
        removal = Toplevel()
        removal.title("Remove")
         
        for dish in self.dish_manager.dish_list:
            btn = Button(removal, text=dish.name, command=lambda i=dish: self.remove_dish(i))
            btn.grid()
            self.dish_buttons[dish] = btn
            self.update_main_menu()
            
    def remove_dish(self, dish):
        self.dish_manager.dish_list.remove(dish)
        self.dish_buttons[dish].destroy()
        del self.dish_buttons[dish]
        self.update_main_menu()