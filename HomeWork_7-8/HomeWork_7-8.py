result = []

def divider(a, b):
    a = int(a)
    b = int(b)
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, 1: 15, 8 : 4}

for key in data:
    try:
        res = divider(key, data[key])
    except (ValueError, IndexError, ZeroDivisionError) as error:
        print(f"Ошыбка. Тип ошибки: {type(error)}")
    else:
        result.append(res)

print(result)