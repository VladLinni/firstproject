from Lesson_2.character import Character

class Vampyre(Character):

    def __init__(self, name="", health=100, damage=1, defence=0):
        Character.__init__(self, name, health, damage, defence)

    def attack(self, target):
        target.get_damage(self.damage)
        self.health += self.damage * 0.1

    def get_stats(self):
        return \
            f'Имя: {self.name}\n' \
            f'Здоровье: {int(self.health)}\n' \
            f'Урон: {self.damage}\n' \
            f'Защита: {self.defence}\n'