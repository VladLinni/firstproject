mss = []
number = ""
summa  = 0
mult = 1
while True:
  if number == 0:
    print('')
    print('Программа закончилась. Вот ваш список:')
    print(mss)
    break
  else:
    number = int(input('Введите любое число(если вы закончили напишите "0"): '))
    mss.append(number)
    summa += number
    mult *= number

answer = input('Что вы хотите сделать с числаи?(умножить или узнать их сумму): ').lower()

if answer == 'сумма':
  print('Сумма чисел:')
  print (summa)
elif answer == 'умножить':
  print('Умножение:')
  print(mult)