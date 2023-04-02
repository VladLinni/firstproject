first = int(input('Введите начальное число: '))
second = int(input('Введите конечное число: '))
summa = 0

print ('')
print ('Диапазон:')
if first < second:
  for i in range(first, second+1):
    print (i)
    summa += i
else:
    for i in range(second, first+1):
      print (i)
      summa += i

print ('')
print (f'Сумма всех чисел диапазона: {summa}')