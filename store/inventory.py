from inventconnect import CURSOR, CONN

class Products:
    def __init__ (self, name, price, quantity,id=None):
        self.id = id 
        self.name = name
        self.price = price
        self.quantity = quantity
      

    def __str__(self):
        return f' name:{self.name} price: {self.price} Qty:{self.quantity} '
    
    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     if isinstance(name, str) and len(name) > 0:  # Check if name is a string and not empty
    #         self._name = name
    #     else:
    #         raise ValueError("Name must be a non-empty string")

    # @property
    # def price(self):
    #     return self._price

    # @price.setter
    # def price(self, price):
    #     if isinstance(price, (int, float)) and price >= 0:
    #         self._price = price
    #     else:
    #         raise ValueError("Price must be a non-negative number")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            quantity TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS products;
        """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        sql = """
                INSERT INTO products (name, price,quantity)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.price, self.quantity))
        CONN.commit()

        self.id = CURSOR.lastrowid
        

    @classmethod #get all products
    def get_all(cls):
        sql = """
            SELECT *
            FROM products
        """

        data= CURSOR.execute(sql)

        return data.fetchall()
    
    @classmethod
    def create_products(cls, name, price, quantity):
        products = cls(name, price, quantity)
        products.save()
        return products
    
    @classmethod
    def get_product_by_id(cls, product_id):
        sql = """
            SELECT * FROM  products WHERE id = ?
        """
        CURSOR.execute(sql, (product_id,))
        product_data = CURSOR.fetchone()
        if product_data:
            # Create and return a Customer object from the fetched data
            return cls(*product_data)
        else:
            return None
        
    @classmethod
    def find_by_name(cls, product_name):
        sql = """
            SELECT *
            FROM products
            WHERE name is ?
        """

        CURSOR.execute(sql, (product_name,))
        product_data = CURSOR.fetchone()
        if product_data:
            # Create and return a Customer object from the fetched data
            return cls(*product_data)
        else:
            return None
    
    def delete(self):
    
        sql = """
            DELETE FROM products
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
   
class Customer:
    def __init__(self, firstName, lastName, id=None):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id

    def __str__(self):
        return f' {self.firstName} {self.lastName}'

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY,
            firstname TEXT,
            lastname TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO customers (firstname, lastname)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.firstName, self.lastName))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM customers
        """

        data= CURSOR.execute(sql)

        return data.fetchall()
     
    @classmethod
    def create_customer(cls, firstName, lastName):
        customer = cls(firstName, lastName)
        customer.save()
        return customer
    
    @classmethod
    def get_customer_by_id(cls, customer_id):
        sql = """
            SELECT * FROM customers WHERE id = ?
        """
        CURSOR.execute(sql, (customer_id,))
        customer_data = CURSOR.fetchone()
        if customer_data:
            return cls(*customer_data)
        else:
                return None
        
    @classmethod
    def find_customer_by_name(cls, firstname):
        sql = """
            SELECT *
            FROM customers
            WHERE firstname = ?
        """

        CURSOR.execute(sql, (firstname,))
        customer_data = CURSOR.fetchone()
        if customer_data:
            return cls(*customer_data)
        else:
            return None

          
class Order:
    def __init__(self, customer_id, product_id, quantity, order_id=None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (product_id) REFERENCES products(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS orders;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO orders (customer_id, product_id, quantity)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.customer_id, self.product_id, self.quantity))
        CONN.commit()

    @classmethod
    def get_all(cls):
        """Return a list containing all orders object per row in the table"""
        sql = """
            SELECT *
            FROM orders
        """

        data = CURSOR.execute(sql)
        orders = []
        for row in data.fetchall():
            order = cls(*row)
            orders.append(order)
        return orders

    @classmethod
    def create_order(cls, customer_id, product_id, quantity):
        order = cls(customer_id, product_id, quantity)
        order.save()
        return order

    @property
    def total_price(self):
        """Calculate the total price for the order"""
        product = Products.get_product_by_id(self.product_id)
        return product.price * self.quantity
    
   


product1 = Products('jelly', 20, 50, 'cooking') 
# print(product1) 
# product1.save(CURSOR, CONN)

customer1 = Customer('karimi', 'kiki' )
# print(customer1)

# order1  = Order(customer1, product1)
# print(order1)


