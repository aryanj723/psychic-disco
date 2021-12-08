class RestaurantController(object):

  def __init__(self, RestaurantService):
    self.restaurant_service = RestaurantService
  
  def addRestaurant(self):
    
    return self.restaurant_service.addRestaurant()

  def getFoodDeliveryTime(self, orders):
    
    #At first, we import all the constraints we have
    restaurant = self.restaurant_service.addRestaurant()
    max_slots = restaurant.getCookingSlots()
    slots_for_A = restaurant.getReqSlotsForA()
    slots_for_M = restaurant.getReqSlotsForM()
    time_for_A = restaurant.getReqTimeForA()
    time_for_M = restaurant.getReqTimeForM()
    delivery_time_per_km = restaurant.getDeliveryTimePerKm()
    max_delivery_time = restaurant.getMaxDeliveryTime()
    food_delivery_time = [0]*max_slots #this mimics the slots in the restaurant
    result = {}# the result is initialized as a dictionary
    
    for order in orders:#iterating over the list of orders
      time_req = 0
      slots_req = 0
      m_present = False
      for meal in order.getMeals():
        
        time_addon = time_for_A if meal =="A" else time_for_M
        time_req = time_req + time_addon
        slot_addon = slots_for_A if meal =="A" else slots_for_M
        slots_req = slots_req + slot_addon
        if meal =="M":
          m_present = True
      
      if slots_req > max_slots:
        result[order.getOrderId()] = "is denied because the restaurant cannot accommodate it"
        continue
      food_delivery_time[0:slots_req] = [food_delivery_time[slots_req -1]] * (slots_req-0)
      max_time_per_slot = time_for_M if m_present else time_for_A # the order is considered to be completed only when all the items are complete, so the max time taken for the order items is the time for preparing the food
      time_taken = food_delivery_time[0] + max_time_per_slot + order.getDistance()*delivery_time_per_km
      
      if(time_taken > max_delivery_time):
        result[order.getOrderId()] = "is denied because processing it will take too much time"
        continue
      
      result[order.getOrderId()] = time_taken
      food_delivery_time[0:slots_req] = [time_taken] * (slots_req-0)#update the status if the slots after taking an order
      food_delivery_time.sort()#this is done to greedily select the least busy slots for next order
    return result