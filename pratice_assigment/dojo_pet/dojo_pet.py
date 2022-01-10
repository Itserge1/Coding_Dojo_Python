from ninja import Ninja
from pet import Pet, Dog



black_night = Ninja( "Black", "night", "yogurt", "pumpkin", Dog("bommy","sit", 100 , 200 ))
# black_night.walk()
# black_night.feed()
black_night.bathe()








# class Ninja:
#     all_ninja = []
#     def __init__(self, first_name, last_name, treats, pet_food, pet):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.treats = treats
#         self.pet_food = pet_food
#         self.pet = pet
#     def walk(self):
#         print(f"{self.first_name} {self.last_name} is walking his {self.pet}")
#         return self
#     def feed(self):
#         print(f"{self.first_name} {self.last_name} is feeding his {self.pet} with some {self.pet_food}")
#         return self
#     def bathe(self):
#         print(f"{self.first_name} {self.last_name} is giving his {self.pet} a shower")
#         return self

# black_night = Ninja( "Black", "night", "yogurt", "pumpkin", "bulldog")
# black_night.walk().feed().bathe()

# class Pet:
#     def __init__(self, name, pet_type, tricks, health, energy):
#         self.name = name
#         self.pet_type = pet_type
#         self.tricks = tricks
#         self.health = health
#         self.energy = energy
#         def sleep():
#             f"{self.name} is sleeping"
#             return self
#         def eat():
#             print(f"{self.name} is eating")
#             return self  
#         def play():
#             print(f"{self.name} is plaing")
#             return self  
#         def noise():
#             print(f"{self.name} is making noise")
#             return self 

