# Authors: Reed Stewart, Perla Valdovinos, Stephanie Pesce, Benjamin Clements
# Decription: This program will give the list of customers and how many hamburgers they ordered

import random
# Create an Order class - REED STEWART
# Create a constructor that defines an instance variable called burger_count
# Create a method called randomBurgers that returns a number between 1 and 20
# The constructor should call the randomBurgers() method and assign the return value to the burger_count instance variable

class Order():
    def __init__(self, burgerCount):
        self.burgerCount = burgerCount

    def randomBurgers():
        return random.randint(1,20)

burger_count = Order.randomBurgers()
print(burger_count)








# Create a Person class - Perla 
# Create a constructor that defines an instance variable called customer_name
# Create a method called randomName() that contains a list of 9 names:
    
class Person():
    def __init__(self): 
        self.customer_name = self.randomName()
        self.randomName() 


# This method randomly returns one of the 9 names when called  - STEPHANIE
# The Person constructor should call the randomName() method and assign the return value (a random name) to the customer_name instance variable

    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

# Create a Customer class that inherits from the Person class
# Create a constructor that calls the parent constructor
# Create an instance variable called order in the constructor that is assigned an order object
class Customer (Person):
    def __init__(self):
        super(). __init__()
        self.order = Order()



# Create a variable for a Queue that will be assigned items of type Customer  - EVAN
# This variable will represent your line of customers (objects) waiting outside to place their hamburger orders
customerQueue = []

iCount = 1

numCustomers = int(input("How many customers are there? "))

for numCustomers in range (0, numCustomers):
    customerQueue.append(Customer.randomName(super))
    iCount = iCount + 1

print(customerQueue)













# Create a variable for a Dictionary with keys of type string and values of type int.  - BENJAMIN
# This variable will hold information about each customer

customerDictionary = {
customerQueue[0] : burger_count,
}

print(customerDictionary)


# customerDictionary = {
# "customerName" : "number of burgers eaten",

# }


















# Put 100 customers into the queue. Each customer object will already have a random number of burgers for each order  - COLLIN
# Make sure there is a key in the dictionary for each customer before you try incrementing their total! Otherwise, add the customer to the dictionary.
# Print out each customer and their total burgers ordered sorted by the most number of burgers ordered
# NOTE: Remember that a queue in Python is a list data structure. Also, the randint() method from the random class returns a random number. For example:




















