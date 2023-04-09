from person import Person
human_1 = Person(name="Васьок", health=100, mood=100, money=10)
print(human_1)
print('')

human_1.change_state(health=-10, mood=-10, money=15)
print(human_1)