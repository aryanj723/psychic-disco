from MyRepo.services.restaurant_service_interface import RestaurantServiceInterface
from MyRepo.models.restaurant import Restaurant

class RestaurantService(RestaurantServiceInterface):
  
  def addRestaurant(self):
    restaurant = Restaurant()
    return restaurant
