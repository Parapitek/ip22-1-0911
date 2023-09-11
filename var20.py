import math

m = float(input('Введите m: '))
n = float(input('Введите n: '))

z1 = ((m-1)*math.sqrt(m) - (n-1)*math.sqrt(n)) / (math.sqrt(m*m*m * n) + m*n + m*m - m)
z2 = (math.sqrt(m) - math.sqrt(n)) / m

print (f'z1 = {z1}')
print (f'z2 = {z2}')