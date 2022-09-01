class Supermarket:
    Supermarkets = {}

    def __init__(self, Code, Name, Address, AddedDate):
        self.Code = Code
        self.Name = Name
        self.Address = Address
        self.AddedDate = AddedDate
        self.Supermarkets[self.Code] = self

    def __str__(self):
        return f"{self.Code};{self.Name};{self.Address};{self.AddedDate};"
