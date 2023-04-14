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

    def change_state(self, action, health=0, mood=0, money=0):
        if self.health + health < 0:
            raise ValueError('умер')
        if self.mood + mood < 0:
            raise ValueError('впал в дипрессию')
        if self.money + money < 0:
            raise ValueError('абонкротился')

        self.health += action.health
        self.mood += action.mood
        self.money += action.money


    def do(self, action):
        if type(Action):
            self.health += action.health
            self.mood += action.mood
            self.money += action.money

            if type(Work) and self.mood > 90:
                self.money += int(action.money * 0.1)
            elif type(Rest) and self.health < 40:
                self.mood += int(action.mood * 0.2)

class Action:
    def __init__(self, name, health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Rest(Action):
    def __init__(self, name, health=0, mood=0, money=0):
        Action.__init__(self, name, health, mood, money)


class Work(Action):
    def __init__(self, name, health=0, mood=0, money=0):
        Action.__init__(self, name, health, mood, money)