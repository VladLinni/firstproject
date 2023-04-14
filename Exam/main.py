from person import Person, Action, Rest, Work
import random

e1 = ''
e2 = ''
e3 = ''

human_1 = Person(name="Вася", health=100, mood=100, money=10)
human_2 = Person(name="Ваня", health=100, mood=100, money=10)
human_3 = Person(name="Влад", health=100, mood=100, money=10)
people = [human_1, human_2, human_3]

go_to_hospital = Action(name='Сходить в больницу', health=20, mood=-10, money=-7)
go_to_park = Rest(name='Сходить в парк', health=5, mood=20, money=-5)
work_on_factory = Work(name='Поработать на заводе', health=-9, mood=-10, money=20)
actions = [go_to_park, go_to_hospital, work_on_factory]

while len(people) > 0:
    if human_1 in people:
        print(f'\n{human_1}')
        try:
            human_1.do(random.choice(actions))
        except ValueError as e:
            print(f'\n{human_1.name} {e}')
            e1 = f'{human_1.name} {e}'
            people.remove(human_1)
    if human_2 in people:
        print(f'\n{human_2}')
        try:
            human_2.do(random.choice(actions))
        except ValueError as e:
            print(f'\n{human_2.name} {e}')
            e2 = f'{human_2.name} {e}'
            people.remove(human_2)
    if human_3 in people:
        print(f'\n {human_3}')
        try:
            human_3.do(random.choice(actions))
        except ValueError as e:
            print(f'\n{human_3.name} {e}')
            e3 = f'{human_3.name} {e}'
            people.remove(human_3)

print(f'\n\n{e1} \n{e2} \n{e3} \n\nВсе люди умерли впали в дипрессию или абонкротились :(')