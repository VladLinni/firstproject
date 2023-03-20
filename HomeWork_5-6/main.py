from Lesson_2.character import Character
from vampyre import Vampyre

character1 = Character(name='Person', health=100, damage=10)
print(character1)
vampyre1 = Vampyre(name='Vampyre', health=100, damage=10)
print(vampyre1)

while character1.is_alive() and vampyre1.is_alive():
    vampyre1.attack(character1)
    character1.attack(vampyre1)
    print(character1)
    print(vampyre1)