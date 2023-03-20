from Lesson_2.character import Character
from berserk import Berserk

character1 = Character(name='Person', health=100, damage=10)
print(character1)
berserk1 = Berserk(name='Berserk', health=100, damage=10)
print(berserk1)

while character1.is_alive() and berserk1.is_alive():
    berserk1.attack(character1)
    character1.attack(berserk1)
    print(character1)
    print(berserk1)