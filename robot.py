class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        print(self.name + " attacked " + dinosaur.type + " with it's " +
              self.weapon.name + " and did " + str(self.weapon.attack_power) + " damage.")
