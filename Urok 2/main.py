from character import Character

player1 = Character(name='Vasya', health=500, damage = 20)
print(player1)
player2 = Character(name='Petya', health=1000, damage = 20)
print(player2)

while player1.is_alive(True) and player2.is_alive(True):
    player2.attack(player1)
    player1.attack(player2)
    print(player1)
    print(player2)