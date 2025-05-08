from tkinter import *
from tkinter import font

class Dish():
    
    Positions_list = []
    Button_list = []
    
    def __init__(self, name):
        self.name = str(name)

    def add_dish_position(self, pos_name):
        pos_name = str(pos_name)
        self.Positions_list.append(pos_name)

    def ret_name(self):
        return self.name

    def make_button(self, window, foo=None):
        btn = Button(window, text=self.name, width=6, height=3, command=foo)
        btn.grid()


        