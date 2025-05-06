class Vehicle:
  def __init__(self, name, speed, capacity):
    self.name = name
    self.speed = speed
    self.capacity = capacity
    self.engine_on = False

  def start_engine(self):
    self.engine_on = True
    return f"{self.name}'s engine is on"

  def stop_engine(self):
    self.engine_on = False
    return f"{self.name}'s engine is off"

  def move(self):
    if self.engine_on:
      return f"{self.name} is moving at {self.speed} its capacity is {self.capacity}"
    else:
      return f"{self.name} cant move you must turn the engine on first"
      
  def stats(self):
      return f"Name: {self.name} \nSpeed: {self.speed} \nCapacity: {self.capacity} \nEngine on: {self.engine_on}"



class Car(Vehicle):
  def __init__(self, name, speed, capacity, fuel_type, num_doors):
    super().__init__(name, speed, capacity)
    self.fuel_type = fuel_type
    self.num_doors = num_doors

  def stats(self):
    parent_output = super().stats()
    return f"{parent_output} \nFuel type: {self.fuel_type} \nNumber of doors: {self.num_doors}"



class Plane(Vehicle):
  def __init__(self, name, speed, capacity, airline, flight_range):
    super().__init__(name, speed, capacity)
    self.airline = airline
    self.flight_range = flight_range
    self.landing_gear_deployed = True
    
  def stats(self):
    parent_output = super().stats()
    return f"{parent_output} \nAirline: {self.airline} \nFight range: {self.flight_range}"

  def take_off(self, direction):
    if self.engine_on:
      self.landing_gear_deployed = False
      return f"{self.name} is taking of in {direction}"
    else:
      return "Can't take off turn engine off first"
    
  def landing(self, airport):
    if self.landing_gear_deployed or not self.engine_on:
      return "Can't land already on the ground"
    else:
      self.landing_gear_deployed = True
      return f"{self.name} is landing in {airport} shortly"
      

  
class Boat(Vehicle):
  def __init__(self, name, speed, capacity, boat_type, anchor_weight):
    super().__init__(name, speed, capacity)
    self.boat_type = boat_type
    self.anchor_weight = anchor_weight
    self.docked = True

  def stats(self):
    parent_output = super().stats()
    return f"{parent_output} \nBoat type: {self.boat_type} \nAnchor weight: {self.anchor_weight}"

  def dock(self):
    if self.engine_on:
      self.docked = False
      return "Can't dock engine is on"
    else:
      self.docked = True
      return "Ship docked"

  def sail(self, direction):
    if self.engine_on and not self.docked:
      return f"{self.name} is setting sail towards {direction}"
    else:
      return "Can't set sail start engine first and undock"

