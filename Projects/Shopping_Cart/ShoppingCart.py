store = {
    'orange' : 25.0,
    'potato' : 53.0,
    'apple' : 33.0,
}
price = {
    'orange' : 5.0,
    'potato' : 2.0,
    'apple' : 3.0,
}
cart = {}

menu = '''
=== Shopping Cart ===
1. Add product
2. Show cart
3. Remove product
4. Total price
5. Exit
'''

while True:
    print(menu)
    choice = input('Enter your choice: ')

    if choice == '1':
     while True:
        print('\n~~~ Items in stock ~~~')
        for key, value in price.items():
            print(f'{key}: {value}' ' $')
        choice_product = input('Select an item or return to the previous menu (press 1): ')
        choice_price = price.get(choice_product)
        if choice_price == price['orange']:
            choice_quantity = input('Enter the weight of the item in kilograms: ')
            if float(choice_quantity) <= 0:
                print('Please enter a positive number')
            elif float(choice_quantity) > store['orange']:
                print ('Sorry, we do not have that many items in stock')
            else:
                cart[choice_product] = float(choice_quantity)
                store['orange'] -= float(choice_quantity)
                print('Thank you, the item has been added to your cart')
        elif choice_price == price['potato']:
            choice_quantity = input('Enter the weight of the item in kilograms: ')
            if float(choice_quantity) <= 0:
                print('Please enter a positive number')
            elif float(choice_quantity) > store['potato']:
                print('Sorry, we do not have that many items in stock')
            else:
                cart[choice_product] = float(choice_quantity)
                store['potato'] -= float(choice_quantity)
                print('Thank you, the item has been added to your cart')
        elif choice_price == price['apple']:
            choice_quantity = input('Enter the weight of the item in kilograms: ')
            if float(choice_quantity) <= 0:
                print('Please enter a positive number')
            elif float(choice_quantity) > store['apple']:
                print('Sorry, we do not have that many items in stock')
            else:
                cart[choice_product] = float(choice_quantity)
                store['apple'] -= float(choice_quantity)
                print('Thank you, the item has been added to your cart')
        elif choice_product == '1':
            break
        else:
            print('Please enter a valid choice')

    elif choice == '2':
        if cart == {}:
            print('The cart is empty')
        else:
            print('~~~ Items in your cart ~~~')
            for key, value in cart.items():
                print(f'{key}: {value}' ' kg')

    elif choice == '3':
        while True:
            if cart == {}:
                print('The cart is empty')
                break
            else:
                print('~~~ Items in your cart ~~~')
                for key, value in cart.items():
                    print(f'{key}: {value}' ' kg')
                Remove_prod = input('Do you want to remove these items? (y/n): ')
                if Remove_prod == 'y':
                    cart = {}
                    print('These items have been removed from your cart')
                    break
                elif Remove_prod == 'n':
                    break
                else:
                    print('Please enter a valid choice\n')

    elif choice == '4':
        if cart == {}:
            print('The cart is empty')
        else:
            orange_price = price.get('orange') * cart.get('orange', 0)
            potato_price = price.get('potato') * cart.get('potato', 0)
            apple_price = price.get('apple') * cart.get('apple', 0)
            total_price = orange_price + potato_price + apple_price
            print(f'The total price is {total_price} $')

    elif choice == '5':
        print('=== Thank you. Goodbye. ===')
        break

    else:
        print('Please enter a valid choice')