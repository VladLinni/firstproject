def input_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(f'Неправельное число. Попробуйте снова!')


a = input_int('Введите A:')
b = input_int('Введите B:')

print(a + b)