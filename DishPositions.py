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
        self.dish_tab.geometry("300x400")

        self.dish_tab.rowconfigure(0, weight=1)
        self.dish_tab.columnconfigure(0, weight=1)
        
        self.canvas = Canvas(self.dish_tab)
        self.scrollbar = Scrollbar(self.dish_tab, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.bottom_frame = Frame(self.dish_tab)
        self.bottom_frame.grid(row=1, column=0, columnspan=2, pady=10)

        self.display()

    def display(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        for widget in self.bottom_frame.winfo_children():
            widget.destroy()

        lbl = Label(self.scrollable_frame, 
            text = f"{self.dish.name} Positions:", 
            anchor = "center",
            width = 30,
            height = 2,
            font = ("PT Sans", 14, "bold")
        )
        lbl.grid(row=0, column=0, columnspan=2)

        row = 1
        for pos, price in self.dish.Positions_list.items():
            dish_btn = Button(self.scrollable_frame, 
                    text = f"{pos}: {price}zl", 
                    command = lambda p=pos, pr=price: self.bill_manager.add_position(p, pr)
            )               
            dish_btn.grid(row=row, column=0, padx=5, pady=2, sticky="w")

            rmv_btn = Button(self.scrollable_frame, 
                    text="-", 
                    command=lambda p=pos: self.remove_position(p)
            )
            rmv_btn.grid(row=row, column=1, padx=(5, 0), pady=2)

            row += 1

        self.name_label = Label(self.bottom_frame, text="Title")
        self.name_label.grid(row=0, column=0, padx=5, pady=(5, 0), sticky="w")
        
        self.name_entry = Entry(self.bottom_frame, width=7)
        self.name_entry.grid(row=1, column=0, padx=5, pady=(0, 5))
        
        self.price_label = Label(self.bottom_frame, text="Price")
        self.price_label.grid(row=0, column=1, padx=5, pady=(5, 0), sticky="w")
        
        self.price_entry = Entry(self.bottom_frame, width=7)
        self.price_entry.grid(row=1, column=1, padx=5, pady=(0, 5))

        self.accept_btn = Button(self.bottom_frame, text="Add position", command=self.add_position)
        self.accept_btn.grid(row=1, column=2, padx=5, pady=(0, 10))

        self.price_entry.bind("<Return>", self.add_position)

    def add_position(self, event=None):
        name = str(self.name_entry.get()).capitalize()
        price = self.price_entry.get()

        if name and price:
            try:
                price = float(price)
            except ValueError:
                print("Has to be a number.")
                return

            if name in self.dish.Positions_list:
                print("Position already exists.")
                return

            self.dish.Positions_list[name] = price
            self.name_entry.delete(0, END)
            self.price_entry.delete(0, END)
            self.display()

    def remove_position(self, position):
        if position in self.dish.Positions_list:
            del self.dish.Positions_list[position]
            self.display()