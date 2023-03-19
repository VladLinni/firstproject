class Character:
    name = ""
    health = 100
    damage = 1
    defence = 0

    def __init__(self, name="", health=100, damage=1, defence=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def __str__(self):
        return self.get_stats()

    def get_stats(self):
        return \
            f'Имя: {self.name}\n' \
            f'Здоровье: {self.health}\n' \
            f'Урон: {self.damage}\n' \
            f'Защита: {self.defence}\n'

    def get_damage(self, damage):
        self.health -= max(damage, 0)

    def attack(self, target):
        target.get_damage(self.damage)

    def is_alive(self):
        return self.health > 0