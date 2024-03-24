from inventory import Products, Customer, Order
from inventconnect import CURSOR, CONN

def exit_program():
    print("ByeBye,see you!!!")
    exit()

# TABLE CRETAION FOR MODELS
def table_creation():
    Products.create_table()
    Customer.create_table()
    Order.create_table()

    # PRODUCTS
def list_products():
    products= Products.get_all()
    for product in products:
        print(product)

def add_products():
    name = input("Enter the product's name: ")
    price = input("Enter the product's price: ")
    quantity = input("Enter the product's quantity: ")
    try:
        # Convert price to float and validate
        price = float(price)
        if price < 0:
            raise ValueError("Price must be a non-negative number")

        products = Products(name, price, quantity)
        products.save()
        print(f'Successfully created product: {products}')
    except ValueError as exc:
        print("Error creating product:", exc)
    except Exception as exc:
        print("Error creating product:", exc)

def get_product_by_id():
    id_ = input("Product id: ")
    product = Products.get_product_by_id(id_)
    print(product) if product else print(f'Product{id_} not found')

def find_product_by_name():
    name = input("Enter the product's name: ")
    product= Products.find_by_name(name)
    print(product) if product else print(
        f'Product {name} not found')

def delete_product():
    id_ = input("Enter product's id: ")
    if product:= Products.get_product_by_id(id_):
        product.delete()
        print(f'Product {id_} deleted')
    else:
        print(f'Product {id_} not found')


        # CUSTOMERS
def list_customers():
    customers= Customer.get_all()
    for customers in customers:
        print(customers)  

def create_customer():
    firstname= input("FirstName: ")
    lastname = input("LastName: ")
   
    try:
        customer = Customer.create_customer(firstname, lastname)
        print(f'Success: {customer}')
    except Exception as exc:
        print("Error creating customer: ", exc)
        
def get_customer_by_id():
    id_ = input("Customer id: ")
    customer = Customer.get_customer_by_id(id_)
    print(customer) if customer else print(f'Customer {id_} not found')

def find_customer_by_name():
    firstname = input("Enter the customer's name: ")
    customer= Customer.find_customer_by_name(firstname)
    print(f'customer name is :{customer}' )if customer else print(
        f'customer {firstname} not found')

def list_orders():
    orders = Order.get_all()
    for order in orders:
        customer = Customer.get_customer_by_id(order.customer_id)
        if customer is not None:
            product = Products.get_product_by_id(order.product_id)
            total_price = product.price * order.quantity
            print(f"Customer: {customer.firstName}")
            print(f"Product: {product.name}")
            print(f"Quantity: {order.quantity}")
            print(f"Total Price: {total_price}")
        else:
            print(f"Customer with ID {order.customer_id} not found")

def place_order():
    try:
        customer_id = int(input("Enter Customer ID: "))
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity: "))

        customer = Customer.get_customer_by_id(customer_id) #Fetch customer details        
       
        product = Products.get_product_by_id(product_id) # # Fetch product details
        
        if customer is not None:
            if product is not None:
                # Calculate total price
                total_price = product.price * quantity
                # Create the order
                order = Order.create_order(customer_id, product_id, quantity)
                print(f'Successfully placed order for   Quantity: {quantity},ProductName: {product.name} and Customer: {customer.firstName} {customer.lastName}')
                print(f'Total Price: {total_price}')

            else:
                print(f"Error placing order: Product with ID {product_id} not found")
        else:
            print(f"Error placing order: Customer with ID {customer_id} not found")
    except Exception as exc:
        print("Error placing order: ", exc)

def main():
    choice = input('Option >> ')
    if choice == "0":
        exit_program()
    elif choice == "1":
        list_products()
    elif choice == "2":
        add_products()
    elif choice == "3":
         get_product_by_id()
    elif choice == "4":
        list_customers()
    elif choice == "5":
        create_customer()
    elif choice == "6":
        get_customer_by_id()
    elif choice == "7":
        find_product_by_name()
    elif choice == "8":
        delete_product()
    elif choice == "9":
        list_orders()
    elif choice == "10":
        place_order()
    elif choice == "11":
       find_customer_by_name()
    
    else:
        print("Invalid choice")
    main()           

if __name__ == '__main__':
    table_creation()

    options = """
0 - exit_program,
1 - list_products,
2 - add_products
3 - get_product_by_id
4 - list_customers
5 - create_customer
6 - get_customer_by_id
7 - find_product_by_name
8 - delete_product
9 - list_orders *
10 - place_order
11 - find_customer_by_name
"""
    print(options)
    main()

# product1 = Products('coffee', 20, 50)
# product2 = Products('sugar', 50, 100)
# product2.save(CURSOR,CONN)
    
    
    