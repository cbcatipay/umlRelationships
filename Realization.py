from abc import ABC, abstractmethod 

class Engine(ABC):
  @abstractmethod
  def start(self): pass

class ElectricEngine(Engine):
  def start(self):
    return "Silent hum... Started!"

car_engine = ElectricEngine()
print(car_engine.start())
