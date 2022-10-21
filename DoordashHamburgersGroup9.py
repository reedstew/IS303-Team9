
#Authors: Reed Stewart, Perla Valdovinos, Colin Gubler, Stephanie Del-Pesce, Benjamin Clements, Evan Carter (With help from special guest, Holy Ghost because this thing was a doozy)
#Description: Team Assignment - Hamburger Doordash!

#Import packages
from audioop import reverse
from multiprocessing.sharedctypes import Value
import random

#Create classes for order, person, and customer
class Order():
    def __init__(self, burgerCount):
        self.burgerCount = burgerCount

    def randomBurgers():
        return random.randint(1,20)

burger_count = Order.randomBurgers()


class Person():
   def __init__(self):
       self.customer_name = ""
       self.randomName()
# This method randomly returns one of the 9 names when called  - STEPHANIE
# The Person constructor should call the randomName() method and assign the return value (a random name) to the customer_name instance variable
   def randomName(self):
       asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
       self.customer_name = random.choice(asCustomers)

# Create a Customer class that inherits from the Person class
# Create a constructor that calls the parent constructor
# Create an instance variable called order in the constructor that is assigned an order object
class Customer (Person):
    def __init__(self):
        super(). __init__()
        self.order = Order.randomBurgers()


# Create a variable for a Queue that will be assigned items of type Customer  - EVAN
# This variable will represent your line of customers (objects) waiting outside to place their hamburger orders
customerQueue = []

for count in range(0,100):
    myCustomer = Customer()
    customerQueue.append(myCustomer)

customerDictionary = {}

while len(customerQueue) > 0:
    # print("A customer was served! ")
    # print(customerQueue[0].customer_name)

    if customerDictionary.get(customerQueue[0].customer_name) ==  None:
        customerDictionary[customerQueue[0].customer_name] = customerQueue[0].order
    else: #IS repeat customer
        newOrder = random.randint(1,20)
        customerDictionary[customerQueue[0].customer_name] += newOrder

    customerQueue.pop(0)

#Sort dictionary by decending order
sortedDictionary = dict(sorted(customerDictionary.items(), key=lambda item: item[1], reverse=True))

#Final Output, seperate lines
for customer in sortedDictionary:
    print(customer, sortedDictionary[customer])


