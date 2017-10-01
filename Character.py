import random


class Character:
    def __init__(self, name, hit_points, attack_bonus, armor):
        self.name = name
        self.hp = hit_points
        self.attack_bonus = attack_bonus
        self.armor = armor

    def roll_dice(self, die):
        return random.randint(1, die)

    def attack(self):
        return self.roll_dice(20) + self.attack_bonus

    def deals_damage(self):
        return self.roll_dice(8) + 4

    def takes_damage(self, damage):
        self.hp -= damage


class Monster(Character):
    def __init__(self, name, hit_points, attack_bonus, armor, kind):
        Character.__init__(self, name, hit_points, attack_bonus, armor)
        self.kind = kind
