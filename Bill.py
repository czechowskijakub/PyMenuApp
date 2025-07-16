class BillManager:
    def __init__(self, bill_path):
        self.bill_path = bill_path
        self.total = 0
        self.lines = []

    def add_position(self, name, price):
        self.lines.append(f"{name}: {price}zl")
        self.total += price

    def save_bill(self):
        with open(self.bill_path, 'w') as f:
            for line in self.lines:
                f.write(line + "\n")
            f.write(f"Total: {self.total}zl\n")
