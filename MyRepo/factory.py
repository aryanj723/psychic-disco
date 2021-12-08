from MyRepo.services.restaurant_service import RestaurantService
from MyRepo.services.order_service import OrderService

class Factory:
  @staticmethod
  def build(obj_type):
    if obj_type == "Restaurant":
      return RestaurantService()
    if obj_type == "Order":
      return OrderService()