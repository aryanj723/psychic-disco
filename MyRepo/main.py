#driver code
import json
import sys
sys.path.append('/home/runner/Aryanrestaurantproblemweekday')
from MyRepo.controllers.order_controller import OrderController
from MyRepo.controllers.restaurant_controller import RestaurantController
from MyRepo.factory import Factory

#using factory pattern to retrive the service
restaurant_controller = RestaurantController(Factory.build("Restaurant"))
order_controller = OrderController(Factory.build("Order"))

#parsing the input
input_file = open('input.txt')
input_data = json.load(input_file)

orders = []#orders would be a list of order class
for entries in input_data:
  orders.append(order_controller.addOrder(entries["orderId"], entries["meals"], entries["distance"]))

restaurant = restaurant_controller.addRestaurant()

#controller is called by client to provide the result in the form of a dictionary
output = restaurant_controller.getFoodDeliveryTime(orders)

for orderId, entry in output.items():
  if(type(entry) != str):#rejection reason is sent as a string.If an order is accepted, a numerical value is sent
    print(f"Order {orderId} will get delivered in {entry} minutes")
  else:
    print(f"Order {orderId} {entry}")
