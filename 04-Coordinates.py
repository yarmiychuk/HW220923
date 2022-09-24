# Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y)

def printResult(quarter, xSymbol, ySymbol):
    print(f'Координаты точек, находящихся в {quarter} четверти: x {xSymbol} 0, y {ySymbol} 0')

quarter = int(input(f'Введите номер четверти координатной плоскости для отображения значений X и Y: '))
if quarter == 1:
    printResult(1, '>', '>')
elif quarter == 2:
    printResult(2, '<', '>')
elif quarter == 3:
    printResult(3, '<', '<')
elif quarter == 4:
    printResult(4, '>', '<')
else:
    print(f'Четверти {quarter} не существует!')