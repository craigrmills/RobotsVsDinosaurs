from robot import Robot
from weapon import Weapon


class Fleet:

    def __init__(self):
        self.robots = []

    def create_fleet(self):
        i = 0
        robots = []
        robot_names = ["Zuckerburg", "Bender", "Kill-a-Tron 5000"]
        names_of_weapons = ["Laspistol", "Chainsword", "Multi-melta"]
        damage_of_weapons = [15, 25, 35]
        while i < 3:
            name = robot_names[i]
            weapon_name = names_of_weapons[i]
            weapon_damage = damage_of_weapons[i]
            robot = Robot(name)
            robot.weapon = Weapon(weapon_name, weapon_damage)
            robots.append(robot)
            i += 1
        self.robots = robots
        pass
