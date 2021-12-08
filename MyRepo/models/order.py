class Order(object):
  
  def __init__(self):
    self.order_id = 0
    self.meals = []
    self.distance = 0

  def setOrderId(self, order_id):
    self.order_id = order_id

  def getOrderId(self):
    return self.order_id

  def setMeals(self, meals):
    self.meals = meals

  def getMeals(self):
    return self.meals

  def setDistance(self, distance):
    self.distance = distance

  def getDistance(self):
    return self.distance
