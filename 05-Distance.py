# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import math

def getCoordinate(point, axis):
    return float(input(f'Введите координату точки {point} по оси {axis}: '))

print('Вычисление расстояния между точками а и b')
ax = getCoordinate('a', 'X')
ay = getCoordinate('a', 'Y')
bx = getCoordinate('b', 'X')
by = getCoordinate('b', 'Y')

print(f'Расстояние между точками равно {math.sqrt((ax - bx) **2 + (ay - by) **2)}')