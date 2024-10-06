import math
from typing import List

class Vector3:
  def __init__(self, x: float = 0, y: float = 0, z: float = 0):
      self.x = x
      self.y = y
      self.z = z

  def __add__(self, other):
      return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

  def __sub__(self, other):
      return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

  def __mul__(self, scalar):
      return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

  @staticmethod
  def zero():
      return Vector3(0, 0, 0)

  @staticmethod
  def normalize(vector):
      magnitude = math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)
      return Vector3(vector.x / magnitude, vector.y / magnitude, vector.z / magnitude)

  @staticmethod
  def distance(a, b):
      return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2)

  def __str__(self):
      return f"({self.x}, {self.y}, {self.z})"

class Swarm:
  def __init__(self):
      self.drones: List[Drone] = []
      self.target_coordinate: Vector3 = Vector3.zero()

  def add_drone(self, drone):
      self.drones.append(drone)
      drone.assign_swarm(self)

  def set_target(self, target: Vector3):
      self.target_coordinate = target
      print(f"Swarm target set to: {target}")

  def start_exploring(self):
      for drone in self.drones:
          drone.start()

class Drone:
  def __init__(self):
      self.swarm: Swarm = None
      self.position: Vector3 = Vector3.zero()
      self.speed: float = 1.0

  def assign_swarm(self, swarm_instance: Swarm):
      self.swarm = swarm_instance

  def start(self):
      while True:
          self.move_towards_swarm_target()
          self.avoid_collision()
          self.take_photo()
          self.send_data_to_rover()

  def move_towards_swarm_target(self):
      if self.swarm is None:
          return

      target = self.swarm.target_coordinate
      direction = Vector3.normalize(target - self.position)
      self.position += direction * self.speed

      if Vector3.distance(self.position, target) < 0.5:
          pass  # Target reached; perform an action if necessary

  def avoid_collision(self):
      # Simple collision avoidance logic
      pass

  def take_photo(self):
      # Capture photo at the current position
      pass

  def send_data_to_rover(self):
      # Send photo data to the rover
      pass

class Rover:
  def __init__(self):
      self.swarm = Swarm()

  def deploy_swarm(self, number_of_drones: int):
      for _ in range(number_of_drones):
          drone = Drone()
          self.swarm.add_drone(drone)

      target_coordinate = Vector3(10, 0, 10)
      self.swarm.set_target(target_coordinate)
      self.swarm.start_exploring()