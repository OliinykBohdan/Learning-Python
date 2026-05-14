class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):

        self.cart.append((product, quantity))
        product.quantity -= quantity
        print(f'Product {product.name} added to cart.')

    def remove_from_cart(self, product, quantity):
        if product not in self.cart:
            print(f'\n{product.name} not in cart.')
            return

        for product in self.cart:
            if product.quantity > quantity:
                product.quantity -= quantity
            print(f'\nThe product quantity "{product.name}" has been changed.')
            return

        print(f'Product {product.name} removed from cart.')
        self.cart.remove(product)
        product.quantity += quantity

    def show_cart(self):
        print('\nProducts in your cart:')
        for product, quantity in self.cart:
            print(f'{product.name} - {quantity}')

class Store:
    def __init__(self):
        self.assortment = []

    def add_to_store(self, product):
        print(f'Product {product.name} added to store.')
        self.assortment.append(product)

    def remove_from_store(self, product):
        if product not in self.assortment:
            print(f'\n{product.name} not in cart.')
            return

        print(f'Product {product.name} removed from cart.')
        self.assortment.remove(product)

    def show_store(self):
        print('\nProducts in store:')
        for product in self.assortment:
            print(f'{product.name} - {product.quantity}')

store = Store()
cart = Cart()

product1 = Product('Milk', 10)
product2 = Product('Potato', 20)

store.add_to_store(product1)
store.add_to_store(product2)

cart.add_to_cart(product1,4)
cart.add_to_cart(product2,5)

cart.show_cart()

store.show_store()
