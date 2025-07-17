from tkinter import *

class Dish:
    def __init__(self, name):
        self.name = str(name)
        self.Positions_list = {}

    def add_dish_position(self, pos_name, price):
        self.Positions_list[pos_name] = price

    def ret_name(self):
        return self.name