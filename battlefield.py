from fleet import Fleet
from herd import Herd
import random


class Battlefield:

    def __init__(self):
        self.fleet = None
        self.herd = None

    def run_game(self):
        fleet = Fleet()
        herd = Herd()
        first_turn = self.display_welcome()
        fleet.create_fleet()
        herd.create_heard()
        self.fleet = fleet
        self.herd = herd
        winner = None
        game_state = True
        while game_state:
            if first_turn == 1:
                self.robo_turn()
                self.dino_turn()
            else:
                self.dino_turn()
                self.robo_turn()
            if self.fleet.robots[0].health <= 0:
                print(self.fleet.robots[0].name + " has exploded!")
                self.fleet.robots.remove(self.fleet.robots[0])
            if self.herd.dinosaurs[0].health <= 0:
                print(self.herd.dinosaurs[0].name + " has met it's end!")
                self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
            if len(self.fleet.robots) < 1:
                winner = "Dinosaurs have Prevailed!"
                game_state = False
            if len(self.herd.dinosaurs) < 1:
                winner = "Robots have Conquered all!"
                game_state = False
        self.display_winners(winner)

    def display_welcome(self):
        print("Welcome to Robots Vs Dinosaurs!\n Enjoy the Fight!\n")
        first_turn = random.randrange(1, 2)
        if first_turn == 1:
            print("The Robots have won the coin toss and shall go first.\n")
        else:
            print("The Dinosaurs have won the coin toss and shall go first.\n")
        return first_turn

    def dino_turn(self):
        if self.herd.dinosaurs[0].health > 0:
            self.herd.dinosaurs[0].attack(self.fleet.robots[0])
        else:
            pass

    def robo_turn(self):
        if self.fleet.robots[0].health > 0:
            self.fleet.robots[0].attack(self.herd.dinosaurs[0])
        else:
            pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self, winner):
        print(winner)
