list = ["book", "car", "apartment", "house"]
answer = 'Y'

while True:
    word = input('Введите слово которое вы хотите найти в списке: ').lower()
    print('Поиск...')
    if word in list:
        print('Это слово есть в списке!')
        answer = input('Хотите проверить ещё одно слово?(Y or N): ').lower()
        print('')
    else:
        print('Этого слова нет в списке!')
        answer = input('Хотите проверить ещё одно слово?(Y or N): ').lower()
        print('')
    if answer == 'n':
        break