from Lesson_2.character import Character
from berserk import Berserk

player1 = Character(name='Person', health=70, damage = 10)
print(player1)
berserk1 = Berserk(name='Berserk', health=90, damage = 8)
print(berserk1)

while player1.is_alive() and berserk1.is_alive():
    berserk1.attack(player1)
    player1.attack(berserk1)
    print(player1)
    print(berserk1)