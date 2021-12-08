class Restaurant(object):
  
  #The reason for them being private members and being initialized in model is that these are private info which need not be exposed publically. Also, setters for them have been disabled for security.
  __cooking_slots = 7
  __req_slots_for_A = 1
  __req_slots_for_M = 2
  __req_time_for_A = 17
  __req_time_for_M = 29
  __delivery_time_per_km = 8
  __max_delivery_time = 180

  def getCookingSlots(self):
    return self.__class__.__cooking_slots
  
  def getReqSlotsForA(self):
    return self.__class__.__req_slots_for_A

  def getReqSlotsForM(self):
    return self.__class__.__req_slots_for_M

  def getReqTimeForA(self):
    return self.__class__.__req_time_for_A

  def getReqTimeForM(self):
    return self.__class__.__req_time_for_M

  def getDeliveryTimePerKm(self):
    return self.__class__.__delivery_time_per_km

  def getMaxDeliveryTime(self):
    return self.__class__.__max_delivery_time
