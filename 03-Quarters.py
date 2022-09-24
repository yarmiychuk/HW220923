# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

def getCoordinate(name):
    return float(input(f'Введите координату по оси {name}: '))

def notInQuarter(axis):
    return f'Точка не находится ни в одной из четвертей и лежит на оси {axis}'

def inQuarter(quarter):
    return f'Точка с указанными координатами находится в {quarter} четверти'

print('В какой четверти координатной плоскости находится точка?')
x = getCoordinate('X')
y = getCoordinate('Y')

if x == 0 and y != 0:
    print(notInQuarter('Y'))
elif x != 0 and y == 0:
    print(notInQuarter('X'))
elif x > 0 and y > 0:
    print(inQuarter(1))
elif x < 0 and y > 0:
    print(inQuarter(2))
elif x < 0 and y < 0:
    print(inQuarter(3))
elif x > 0 and y < 0:
    print(inQuarter(4))
else:
    print('Вы ввели координаты точки начала координат')

