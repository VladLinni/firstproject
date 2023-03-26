while True:
    file_name = input('Введите название файла:')

    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print('Файла не существует')
        answer = input('Хотите попробовать ещё раз?(y or n)')
        if answer == 'n':
            break
    else:
        print(f'Открываем файл: {file_name}')
        print('Содержимое файла:\n')
        for line in file.readlines():
            print(line.strip())

        file.close()
        break