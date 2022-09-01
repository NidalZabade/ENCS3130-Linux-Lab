import datetime
from Warehouse import *
from SuperMarket import *

WarehouseFile = open("warehouse_items.txt", "r")
for line in WarehouseFile:
    line = line.strip()
    Split = line.split(";")
    Date = datetime.datetime.strptime(Split[2], "%d/%m/%Y").strftime("%d/%m/%Y")
    Warehouse(Split[0], Split[1], Date, float(Split[3]), float(Split[4]), int(Split[5]))


def AddItem():
    ItemCode = None
    ItemName = None
    ItemDate = None
    ItemCost = None
    ISU = None
    ItemQuantity = None
    while True:
        Code = input("Enter Item Code\n")
        if Code in Warehouse.Items:
            print(f"There such Item {str(Warehouse.Items[Code])}\ntry again\n")
            continue
        if Code.isdigit() and len(Code) == 4:
            ItemCode = Code
            break
        else:
            print("The Code must be only 4 digits")
            continue
    while True:
        Name = input("Enter Item Name\n")
        if Name.isalpha():
            ItemName = Name
            break
        else:
            print("The Name should be in alphabet")
            continue
    while True:
        Date = input("Enter date in form dd/mm/yyyy\n")
        try:
            Date = datetime.datetime.strptime(Date, "%d/%m/%Y").strftime("%Y/%m/%d")
            if Date > datetime.datetime.now().strftime("%Y/%m/%d"):
                ItemDate = datetime.datetime.strptime(Date, "%Y/%m/%d").strftime("%d/%m/%Y")
                break
            else:
                print("The Expiry Date you enterd is today or in the past\ntry again")
                continue
        except ValueError:
            print("The Expiry Date you enterd is not Valid\ntry again")
            continue
    while True:
        Cost = input("Enter Item Cost\n")
        if Code.isdigit():
            ItemCost = float(Cost)
            break
        else:
            print("The Cost must be number")
            continue

    while True:
        IS = input("Enter Item Sales Unit Cost (ISU)\n")
        if IS.isdigit():
            if IS > Cost:
                ISU = float(IS)
                break
            else:
                print(f"There is no profit because the cost is {ItemCost}\ntry again")
        else:
            print("The ISU must be number")
            continue
    while True:
        Quantity = input("Enter Item Quantity\n")
        if Code.isdigit():
            ItemQuantity = int(Quantity)
            break
        else:
            print("The Quantity must be number")
            continue
    Warehouse(ItemCode, ItemName, ItemDate, ItemCost, ISU, ItemQuantity)


def AddSupermarket():
    SupermarketCode = None
    SupermarketName = None
    SupermarketAdress = None
    SupermarketDate = None
    while True:
        Code = input("Enter Supermarket Code\n")
        if Code in Supermarket.Supermarkets:
            print(f"There such Supermarket {str(Supermarket.Supermarkets[Code])}\ntry again\n")
            continue
        if Code.isdigit():
            SupermarketCode = Code
            break
        else:
            print("The Code must be only digits")
            continue
    while True:
        Name = input("Enter Supermarket Name\n")
        if Name.isalpha():
            SupermarketName = Name
            break
        else:
            print("The Name should be in alphabet")
            continue
    while True:
        Date = input("Enter date in form dd/mm/yyyy\n")
        try:
            Date = datetime.datetime.strptime(Date, "%d/%m/%Y").strftime("%Y/%m/%d")
            if Date <= datetime.datetime.now().strftime("%Y/%m/%d"):
                SupermarketDate = datetime.datetime.strptime(Date, "%Y/%m/%d").strftime("%d/%m/%Y")
                break
            else:
                print("The time you add the supermarket cannot be in the future\ntry again")
                continue
        except ValueError:
            print("The Date you enterd is not Valid\ntry again")
            continue
    while True:
        Address = input("Enter Supermarket Address\n")
        SupermarketAdress = Address
        break
    Supermarket(SupermarketCode, SupermarketName, SupermarketAdress, SupermarketDate)
    filename = f"DistributeItems_{SupermarketCode}.txt"
    f = open(filename, "w")
    f.close()


def List():
    TotalWholesale = 0
    TotalSaleCost = 0

    while True:
        Date = input("Enter date in form dd/mm/yyyy\n")
        try:
            Date = datetime.datetime.strptime(Date, "%d/%m/%Y").strftime("%Y/%m/%d")
            print(
                f"List of item  that have an expiry date before {datetime.datetime.strptime(Date, '%Y/%m/%d').strftime('%d/%m/%Y')}:-\n")
            for item in Warehouse.Items.values():
                if Date > datetime.datetime.strptime(item.ExpiryDate, "%d/%m/%Y").strftime("%Y/%m/%d"):
                    print(str(item))
                    TotalWholesale = TotalWholesale + (item.Cost * item.Quantity)
                    TotalSaleCost = TotalSaleCost + (item.ISU * item.Quantity)
            break
        except ValueError:
            print("The Date you enterd is not Valid\ntry again")
            continue
    print(f"The total wholesale cost: {TotalWholesale}\nThe total sales cost: {TotalSaleCost}")


def Clear():
    while True:
        Code = input("Enter Item Code\n")
        if Code in Warehouse.Items and Code.isdigit() and len(Code) == 4:
            print(f"{str(Warehouse.Items[Code])}\n")
            break
        elif Code not in Warehouse.Items and Code.isdigit():
            print("There no such item\n")
            return
        else:
            print("The Code must be only 4 digits")
            continue
    Q = int(input(
        f"Enter the quantity of the item you need cleared\n(The maximum you can clear of this item is {Warehouse.Items[Code].Quantity})\n"))

    if Q > Warehouse.Items[Code].Quantity:
        print(f"maximum you can clear of this item is {Warehouse.Items[Code].Quantity}")
    else:
        Warehouse.Items[Code].Quantity = Warehouse.Items[Code].Quantity - Q
        print(
            f"You cleard {Q} of {Warehouse.Items[Code].Code}:{Warehouse.Items[Code].Name} you have {Warehouse.Items[Code].Quantity} remain\n")


def Distribute():
    for supermarket in Supermarket.Supermarkets:
        file = open(f"DistributeItems_{supermarket}.txt", "r")
        print(f"Supermarket {supermarket} Distribution")
        for line in file:
            line = line.strip()
            Split = line.split(";")
            if Split[0] in Warehouse.Items:
                if Warehouse.Items[Split[0]].Quantity == 0:
                    print(f"There is no remain item with code {Split[0]} in the warehouse")
                elif Split[1] <= Warehouse.Items[Split[0]].Quantity and Warehouse.Items[Split[0]].Quantity > 0:
                    Warehouse.Items[Split[0]].Quantity = Warehouse.Items[Split[0]].Quantity - Split[1]
                    print(f"{Split[0]}: {Split[1]} is avalible is the warehouse")
                else:
                    Q = Warehouse.Items[Split[0]].Quantity
                    Warehouse.Items[Split[0]].Quantity = Warehouse.Items[Split[0]].Quantity - Warehouse.Items[
                        Split[0]].Quantity
                    print(
                        f"There is not enough {Warehouse.Items[Split[0]].Name} in the warehouse only {Warehouse.Items[Split[0]].Quantity} were avalible")
            else:
                print(f"There is no such item with code {Split[0]} with quantity {Split[1]} in the warehouse")


def Report():
    TotalItem = 0
    TotalWholesale = 0
    TotalSales = 0
    for item in Warehouse.Items.values():
        TotalItem = TotalItem + item.Quantity
        TotalWholesale = TotalWholesale + (item.Quantity * item.Cost)
        TotalSales = TotalSales + (item.Quantity * item.ISU)

    print(f"Total items= {TotalItem}")
    print(f"Total wholesale= {TotalWholesale}")
    print(f"Total sales= {TotalSales}")
    print(f"Total profit= {TotalSales - TotalWholesale}")



