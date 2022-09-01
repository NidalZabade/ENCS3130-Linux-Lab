class Warehouse:
    Items = {}

    def __init__(self, Code, Name, ExpiryDate, Cost, ISU, Quantity):
        self.Code = Code
        self.Name = Name
        self.ExpiryDate = ExpiryDate
        self.Cost = Cost
        self.ISU = ISU
        self.Quantity = Quantity
        self.Items[self.Code] = self

    def __str__(self):
        return f"{self.Code};{self.Name};{self.ExpiryDate};{self.Cost};{self.ISU};{self.Quantity}"
