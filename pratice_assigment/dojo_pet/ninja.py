class Ninja:
    all_ninja = []
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        print(f"{self.first_name} {self.last_name} is walking his {self.pet.name}")
        return self
    def feed(self):
        print(f"{self.first_name} {self.last_name} is feeding his {self.pet.name} with some {self.pet_food}")
        return self
    def bathe(self):
        print(f"{self.first_name} {self.last_name} is giving his {self.pet.name} a shower")
        return self