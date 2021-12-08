class OrderController(object):
  def __init__(self, OrderService):
    self.order_service = OrderService
  
  def addOrder(self, order_id, meals, distance):
    return self.order_service.addOrder(order_id, meals, distance)
