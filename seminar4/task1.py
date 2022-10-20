#Вычислить число c заданной точностью d

from decimal import Decimal

num_str = input('Введите число: ')

accuracy = input('Введите точность вычисления в формате 0.0...01: ')

print( Decimal(num_str).quantize( Decimal(accuracy) ) )
