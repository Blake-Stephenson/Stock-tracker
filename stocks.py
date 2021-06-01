class StockBank:
    def __init__(self):
        self.index = 0
        self.bank = []

    def next(self):
        if len(self.bank) < 1:
            return
        self.index += 1
        if self.index >= len(self.bank):
            self.index = 0

    def add_stock(self, string):
        self.bank.append(string)

    def add_file(self, fileName):
        f = str(open(fileName, "r").read())
        self.bank = f.split("\n")

    def get(self):
        return self.bank[self.index]

    def get_bank(self):
        return self.bank
