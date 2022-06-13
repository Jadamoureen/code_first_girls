#Takes in 3 items and their prices and gives a detailed output with total amount

def cashier_receipt():
    item1_name = input('Enter the name of the first item: ')
    item1_price = float(input('Enter the price of the first item: '))
    item2_name = input('Enter the name of the second item: ')
    item2_price = float(input('Enter the price of the second item: '))
    item3_name = input('Enter the name of the third item: ')
    item3_price = float(input('Enter the price of the third item: '))
    Total = item1_price + item2_price + item3_price
    print(f"\n {item1_name} {item1_price} \n {item2_name} {item2_price} \n {item3_name} {item3_price}\n Total {Total}")
    # print(item1_name, item1_price)
    # print(item2_name,item2_price)
    # print(item3_name, item3_price)
    # print("Total" , Total)
cashier_receipt()