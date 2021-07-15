from dinosaur import Dinosaur
import random


class Herd:

    def __init__(self):
        self.dinosaurs = []

    def create_heard(self):
        i = 0
        dinosaurs = []
        dinosaur_names = ["Long-neck", "Trihorn", "Sharp-Tooth"]
        damage_of_dinosaurs = [random.randrange(
            5, 15), random.randrange(10, 25), random.randrange(15, 35)]
        while i < 3:
            name = dinosaur_names[i]
            dino_damage = damage_of_dinosaurs[i]
            dinosaur = Dinosaur(name, dino_damage)
            dinosaurs.append(dinosaur)
            i += 1
        self.dinosaurs = dinosaurs
        pass
