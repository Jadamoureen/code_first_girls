def cashier_receipt(item1_name,item2_name,item3_name):

    #item1_name = input('Enter the name of the first item: ')
    item1_price = float(input('Enter the price of the first item: '))
    #item2_name = input('Enter the name of the second item: ')
    item2_price = float(input('Enter the price of the second item: '))
    #item3_name = input('Enter the name of the third item: ')
    item3_price = float(input('Enter the price of the third item: '))

    Total = 'TOTAL' + ' ' + str(item1_price + item2_price + item3_price)
    item1 = item1_name + ' ' + str(item1_price)
    item2 = item2_name + ' ' + str(item2_price)
    item3 = item3_name + ' ' + str(item3_price)
    together = '{} \n{} \n{} \n{}'.format(item1, item2, item3, Total)
    return together
item1_name = input('Enter the name of the first item: ')
item2_name = input('Enter the name of the second item: ')
item3_name = input('Enter the name of the third item: ')

print_out = cashier_receipt(item1_name,item2_name,item3_name)
print(print_out)