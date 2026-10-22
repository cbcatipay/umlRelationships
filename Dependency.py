class GasStation:
  def refill(self):
    return "Fuel tank filled up!"

class Car:
  def drive_to_station(self, station: GasStation):
    result = station.refill()
    print(f"Car action: {result}")

my_car = Car()
local_station = GasStation()
