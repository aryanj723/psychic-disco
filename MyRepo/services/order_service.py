from MyRepo.services.order_service_interface import OrderServiceInterface
from MyRepo.models.order import Order

class OrderService(OrderServiceInterface):

  order_details = {}

  def addOrder(self, order_id, meals, distance):
    order = Order()
    order.setOrderId(order_id)
    order.setMeals(meals)
    order.setDistance(distance)
    self.__class__.order_details[order_id] = order
    return order
