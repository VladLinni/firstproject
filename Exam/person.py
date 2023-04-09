class Person:
    name = ''
    health = 0
    mood = 0
    money = 0

    def __init__(self, name="", health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return \
            f'Имя: {self.name}\n' \
            f'Здоровье: {self.health}\n' \
            f'Настроение: {self.mood}\n' \
            f'Деньги: {self.money}'

    def change_state(self, health, mood, money):
        if self.health < 0:
            raise SyntaxError('Человек умер')
        if self.mood < 0:
            raise ValueError('Человек впал в депрессию')
        if self.money < 0:
            raise TypeError('Человек обанкротился')

        self.health += health
        self.mood += mood
        self.money += money
