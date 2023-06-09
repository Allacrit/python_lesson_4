"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по
окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
"""

from random import randint

n = int(input('Введите кол-во кустов: '))
a = list()
for i in range(n):
    num_barries = randint(7,25)
    print(f'На кусте №{i + 1} кол-во ягод {num_barries}.')
    a.append(num_barries)

a_count = list()
for i in range(len(a) - 1):
    a_count.append(a[i - 1] + a[i] + a[i + 1])
a_count.append(a[-2] + a[-1] + a[0])

print(f'Максимальное кол-во ягод которое может собрать модуль: {max(a_count)}.')
