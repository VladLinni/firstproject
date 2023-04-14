from person import Person, Action, Rest, Work
import random
from colorama import Fore

e1 = ''
e2 = ''
e3 = ''

human_1 = Person(name="Вася", health=100, mood=100, money=10)
human_2 = Person(name="Ваня", health=100, mood=100, money=10)
human_3 = Person(name="Влад", health=100, mood=100, money=10)
people = [human_1, human_2, human_3]

go_to_hospital = Action(name='Сходить в больницу', health=20, mood=-5, money=-20)
go_to_park = Rest(name='Сходить в парк', health=3, mood=15, money=0)
work_on_factory = Work(name='Поработать на заводе', health=-3, mood=-10, money=50)
actions = [go_to_park, go_to_hospital, work_on_factory]

print('-----Real Life Simulator-----', Fore.MAGENTA)

while len(people) > 0:
    if human_1 in people:
        print(f'\n{human_1}', Fore.BLUE)
        try:
            human_1.do(random.choice(actions))
        except ValueError as e:
            print(f'\n{human_1.name} {e}')
            e1 = f'{human_1.name} {e} {Fore.RED}'
            print(e1)
            people.remove(human_1)
    if human_2 in people:
        print(f'\n{human_2}', Fore.GREEN)
        try:
            human_2.do(random.choice(actions))
        except ValueError as e:
            print(f'\n{human_2.name} {e}')
            e2 = f'{human_2.name} {e} {Fore.RED}'
            print(e2)
            people.remove(human_2)
    if human_3 in people:
        print(f'\n {human_3}', Fore.YELLOW)
        try:
            human_3.do(random.choice(actions))
        except ValueError as e:
            e3 = f'{human_3.name} {e}'
            print(e3)
            people.remove(human_3)

print(f'\n\n{e1} \n{e2} \n{e3} \n\nВсе люди умерли впали в дипрессию или абонкротились :( {Fore.RED}')