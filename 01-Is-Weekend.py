# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

def getName(number):
    dayNames = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return dayNames[number - 1]

def isWeekend(number):
    if number < 6:
        return "РАБОЧИЙ день"
    return "ВЫХОДНОЙ день"
    
dayOfWeek = int(input('Введите число, обозначающее день недели (1-7): '))
if dayOfWeek < 1 and dayOfWeek > 7:
    print("Такого дня недели не существует!")
else:
    print (f'{dayOfWeek} день недели это {getName(dayOfWeek)}, и это {isWeekend(dayOfWeek)}')