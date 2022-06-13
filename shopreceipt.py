def reciept(Item_1_name, Item_2_name, Item_3_name):
    Item_1_price = 50.45
    Item_2_price = 12
    Item_3_price = 80.55
    total = 'Total', Item_1_price + Item_2_price + Item_3_price
    return Item_1_name, Item_1_price, Item_2_name, Item_2_price, Item_3_name, Item_3_price, total


reciept("Trainers", "T-Shirt", "Boots")