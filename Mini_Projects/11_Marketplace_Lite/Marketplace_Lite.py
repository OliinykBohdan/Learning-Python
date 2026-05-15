class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = []

    def add_to_store(self, product):
        for existing_product in self.products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                print(f'\nProduct "{product.name}" quantity updated in store.')
                return

        self.products.append(product)
        print(f'\nProduct "{product.name}" added to store.')

    def show_store(self):
        print('\n=== Products in store ===')

        if not self.products:
            print('Store is empty.')
            return

        for product in self.products:
            print(f'{product.name} - {product.quantity}')

class Cart:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self, product, quantity):

        if quantity <= 0:
            print('\nQuantity must be greater than 0.')
            return

        if quantity > product.quantity:
            print(f'\nNot enough "{product.name}" in stock.')
            return

        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

        product.quantity -= quantity

        print(f'\nAdded {quantity} "{product.name}" to cart.')

    def remove_from_cart(self, product, quantity):

        if product not in self.cart:
            print(f'\n"{product.name}" not found in cart.')
            return

        if quantity > self.cart[product]:
            print(f'\nThere are not that many "{product.name}" in the cart.')
            return

        self.cart[product] -= quantity
        product.quantity += quantity

        if self.cart[product] == 0:
            del self.cart[product]

        print(f'\nRemoved {quantity} "{product.name}" from cart.')

    def show_cart(self):
        print('\n=== Products in cart ===')

        if not self.cart:
            print('Cart is empty.')
            return

        for product, quantity in self.cart.items():
            print(f'{product.name} - {quantity}')

store = Store()
cart = Cart()

product1 = Product('Milk', 10)
product2 = Product('Bread', 5)
product3 = Product('Apple', 20)

store.add_to_store(product1)
store.add_to_store(product2)
store.add_to_store(product3)

store.show_store()

cart.add_to_cart(product1, 3)
cart.add_to_cart(product1, 2)
cart.add_to_cart(product2, 1)

cart.show_cart()

store.show_store()

cart.remove_from_cart(product1, 4)

cart.show_cart()

store.show_store()
