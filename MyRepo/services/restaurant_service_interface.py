import abc

class RestaurantServiceInterface(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def addRestaurant(self):
    pass
