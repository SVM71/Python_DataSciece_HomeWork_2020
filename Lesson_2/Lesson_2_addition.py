import pandas as pd
import numpy as np
import random as rnd
from matplotlib import pyplot as plt

# 1. Создать одномерный массив Numpy под названием a из 12 последовательных целых чисел
# чисел от 12 до 24 невключительно
a = np.array(range(12,24))
print(f'a: {a}')

# 2. Создать 5 двумерных массивов разной формы из массива a. Не использовать в аргументах
# метода reshape число -1.
a_12_1 = np.reshape(a, (12,1))
print(f'a_12_1: {a_12_1}')
a_2_6 = np.reshape(a, (2,6))
print(f'a_2_6: {a_2_6}')
a_6_2 = np.reshape(a, (6,2))
print(f'a_6_2: {a_6_2}')
a_3_4 = np.reshape(a, (3,4))
print(f'a_3_4: {a_3_4}')
a_4_3 = np.reshape(a, (4,3))
print(f'a_4_3: {a_4_3}')
# 3. Создать 5 двумерных массивов разной формы из массива a. Использовать в аргументах
# метода reshape число -1 (в трех примерах - для обозначения числа столбцов, в двух - для
# строк).
a_4_3 = np.reshape(a, (4,-1))
a_3_4 = np.reshape(a, (3,-1))
a_6_2 = np.reshape(a, (6,-1))
a_2_6 = np.reshape(a, (2,-1))
a_12_1 = np.reshape(a, (12,-1))

# 4. Можно ли массив Numpy, состоящий из одного столбца и 12 строк, назвать одномерным?
# run: help(np.reshape)
# If an integer, then the result will be a 1-D array of that length.
# One shape dimension can be -1. In this case, the value is
# inferred from the length of the array and remaining dimensions.
# ОТВЕТ: НЕЛЬЗЯ, поскольку имеет два индекса.

# 5. Создать массив из 3 строк и 4 столбцов, состоящий из случайных чисел с плавающей запятой
# из нормального распределения со средним, равным 0 и среднеквадратичным отклонением,
# равным 1.0. Получить из этого массива одномерный массив с таким же атрибутом size, как и
# исходный массив.

arr_3_4 = np.random.normal( loc = 0.0, scale = 1.0, size = (3,4) )
print(f'Array_3_4: {arr_3_4}')
print(f'One dimension array: {arr_3_4.flatten()}')

# 6. Создать массив a, состоящий из целых чисел, убывающих от 20 до 0 невключительно с интервалом 2.
arr_a = np.array([ a for a in range(20, 0, -2) ])
print( arr_a )

# 7. Создать массив b, состоящий из 1 строки и 10 столбцов: целых чисел, убывающих от 20 до 1
# невключительно с интервалом 2. В чем разница между массивами a и b?
arr_b = np.array([[ a for a in range(20, 0, -2) ],])
print( arr_b )
# Отличие одномерный и не одномерный массив.

# 8. Вертикально соединить массивы a и b. a - двумерный массив из нулей, число строк которого
# больше 1 и на 1 меньше, чем число строк двумерного массива b, состоящего из единиц.
# Итоговый массив v должен иметь атрибут size, равный 10.
a = np.array( [ np.ones_like(0) for _ in range(8) ] ).reshape(4,2)
b = np.array( [ np.zeros_like(0) for _ in range(2) ] )
c = np.vstack((a,b))
print( f' result of np.vstack((a,b)):\n{c}, \nres_size: {c.size}' )

# 9. Создать одномерный массив а, состоящий из последовательности целых чисел от 0 до 12.
# Поменять форму этого массива, чтобы получилась матрица A (двумерный массив Numpy),
# состоящая из 4 строк и 3 столбцов. Получить матрицу At путем транспонирования матрицы A.
# Получить матрицу B, умножив матрицу A на матрицу At с помощью матричного умножения.
# Какой размер имеет матрица B? Получится ли вычислить обратную матрицу для матрицы B и
# почему?
A = np.array( [ x for x in range(12) ] ).reshape(4,3)
At = np.transpose(A)
print('\n',20*'=','\n', A, '\n',20*'=','\n', At)

B = np.matmul( At, A )
print('\n',20*'=','\n', B.size, B.shape, B)
B_ = np.linalg.inv(B)
B_t = (np.linalg.inv(B)).T
print('\n',20*'=','\n', B_)
print('='*20)
print( f' (At)-1 == (A-1)t:   { (B_t == B_) }'  )



# 10. Инициализируйте генератор случайных числе с помощью объекта seed, равного 42.
# 11. Создайте одномерный массив c, составленный из последовательности 16-ти случайных
# равномерно распределенных целых чисел от 0 до 16 невключительно.

# help(np.random.seed)
# >> > from numpy.random import MT19937
# >> > from numpy.random import RandomState, SeedSequence
# >> > rs = RandomState(MT19937(SeedSequence(123456789)))
# # Later, you want to restart the stream
# >> > rs = RandomState(MT19937(SeedSequence(987654321)))
np.random.seed(42)
rA = np.array([np.random.randint(0,16) for  _ in range(16)])
print(rA)

# 12. Поменяйте его форму так, чтобы получилась квадратная матрица C. Получите матрицу D,
# поэлементно прибавив матрицу B из предыдущего вопроса к матрице C, умноженной на 10.
# Вычислите определитель, ранг и обратную матрицу D_inv для D.
C = rA.reshape(4,4)
print(C)
D = 10*C
print(D, np.linalg.det(D), np.linalg.matrix_rank(D), np.linalg.inv(D))

# 13. Приравняйте к нулю отрицательные числа в матрице D_inv, а положительные - к единице.
# Убедитесь, что в матрице D_inv остались только нули и единицы.
# С помощью функции  numpy.where, используя матрицу D_inv в качестве маски, а матрицы B и C - в качестве
# источников данных, получите матрицу E размером 4x4. Элементы матрицы E, для которых
# соответствующий элемент матрицы D_inv равен 1, должны быть равны соответствующему
# элементу матрицы B, а элементы матрицы E, для которых соответствующий элемент матрицы
# D_inv равен 0, должны быть равны соответствующему элементу матрицы C.
D_ = np.linalg.inv(D)
Dx = (D_ > 0).astype(int)
print( Dx )
Dy = np.where( Dx == 0, C, D_ )
print( Dy )



