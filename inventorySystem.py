class Product:
    '''
    this is a class for product.
    it contains name, price, quantity and type of a product
    '''
    def __init__(self, name, price, quantity, product_type):
        self.name = name
        self.price = float(price.split(' ')[0])
        self.quantity = int(quantity)
        self.type = product_type

    def __str__(self):
        return f"{self.name}, {self.price} RS, {self.quantity}, {self.type}"

def print_products(products):
    '''
    this function prints all the products in the product list/inventory
    '''
    print("List of the products:")
    for product in products:
        print(product)

def get_product(products, product_name):
    '''
    this function returns a particular product by its name
    '''
    for product in products:
        if product.name.lower() == product_name.lower():
            product_available = True
            return product
    return None  # handles if there is no such product that has been searched for

def add_product(products, new_product):
    '''
    this function adds a new product to the products list
    '''
    products.append(new_product)
    print(f"Product: {new_product.name} has been added successfully.\n")

def remove_product(products, product_name):
    '''
    this function removes an existing product from the products list
    '''
    product = get_product(products,product_name)
    if product == None:
        print(f"{product_name} is not available. So, can't be removed.\n")
        return
    products.remove(product)
    print(f"Product: {product.name} has been removed successfully.\n")
        
def filter_by_type(products, product_type):
    '''
    this function filters all the products of same type from the products list
    '''
    filtered_products = []
    for product in products:
        if product.type.lower() == product_type.lower():
            filtered_products.append(product)
    return filtered_products

def update_quantity(products, product_name, quantity):
    '''
    this function updates quantity of an existing product
    '''
    product = get_product(products, product_name)
    if product == None:
        print(f"{product_name} is not available. So, can't be updated. Add the product first\n")
        return
    product.quantity += quantity

def calculate_total_cost(products, items):
    '''
    this function calculates cost of all items added into the user cart
    '''
    total_cost = 0
    for item in items:
        product = get_product(products, item[0])
        total_cost += item[1] * product.price
    return round(total_cost)

# Initial list of products
products = [
    Product("lettuce", "10.5 RS", 50, "Leafy green"),
    Product("cabbage", "20 RS", 100, "Cruciferous"),
    Product("pumpkin", "30 RS", 30, "Marrow"),
    Product("cauliflower", "10 RS", 25, "Cruciferous"),
    Product("zucchini", "20.5 RS", 50, "Marrow"),
    Product("yam", "30 RS", 50, "Root"),
    Product("spinach", "10 RS", 100, "Leafy green"),
    Product("broccoli", "20.2 RS", 75, "Cruciferous"),
    Product("garlic", "30 RS", 20, "Leafy green"),
    Product("silverbeet", "10 RS", 50, "Marrow"),
]

# 1. Print the total number of products in the list.
print("Total number of products in the list: ", len(products), "\n")

# 2. Add a new product and print the list of all products and the total number of products.
new_product = Product("Potato", "10 RS", 50, "Root")
add_product(products, new_product)
print_products(products)
print("Total number of products in the list: ", len(products), "\n")

# 3. Print all the products of which have the type Leafy green.
leafy_green_products = filter_by_type(products, "Leafy green")
print_products(leafy_green_products)

# 4. Remove Garlic from the list and print the total number of products that are left.
remove_product(products, "garlic")
print("Total number of products that are left in the list: ", len(products), "\n")

# 5. Add 50 cabbages to the inventory and print the final quantity of cabbage.
update_quantity(products, "cabbage", 50)
final_quantity_cabbage = get_product(products, "cabbage").quantity
print("Final quantity of cabbage : ", final_quantity_cabbage, "\n")

# 6. Calculate the total cost for a user purchasing items.
user_items = [("lettuce", 1), ("zucchini", 2), ("broccoli", 1)]
total_cost = calculate_total_cost(products, user_items)
print(f"Total cost for the user: {total_cost} RS \n")