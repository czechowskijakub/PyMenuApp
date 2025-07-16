from Dish import *

class DishOptions:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.dish_list = []
        
    def save_profile(self):
        with open(self.csv_file, 'w') as file:
            for dish in self.dish_list:
                file.write(f"{dish.name},")
                for position, price in dish.Positions_list:
                    file.write(f"{position},{price},")
                file.write("\n")
                
    def load_profile(self):
        try:
            with open(self.csv_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    attributes = line.split(",")
                    dish_ctgry = Dish(attributes[0])
                    for i in range(1, len(attributes)-1, 2):
                        try:
                            name = attributes[i]
                            price = float(attributes[i+1])
                            dish_ctgry.add_dish_position(name, price)
                        except (ValueError, IndexError):
                            print(f"Err in line: {line}")
                    self.dish_list.append(dish_ctgry)
        except FileNotFoundError:
            print("No profile file found.")
    
    def add_dish(self, dish):
        if dish not in self.dish_list:
            self.dish_list.append(dish)

    def remove_dish(self, dish_name):
        if dish_name in self.dish_list:
            self.dish_list.remove(dish_name)
        else:
            print("Nothing to remove.")
        