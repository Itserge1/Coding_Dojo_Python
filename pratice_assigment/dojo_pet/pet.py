class Pet:
    def __init__(self, name, tricks, health, energy):
        self.name = name
        self.tricks = tricks
        self.health = 100
        self.energy = 200
        self.noise = ""
    def sleep(self):
        f"{self.name} is sleeping"
        return self
    def eat(self):
        print(f"{self.name} is eating")
        return self  
    def play(self):
        print(f"{self.name} is plaing")
        return self  
    def make_noise(self):
        print(self.noise)
        return self.noise

class Dog(Pet):
    def __init__(self,name, tricks, health, energy):
        super().__init__(name, tricks, health, energy)
        self.noise = "bark"
