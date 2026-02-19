import numpy as np

a = np.array([1, 4, 9, 16, 25])
b = np.array([2, 4, 6, 8, 10])


print('La suma de elemento a elemento de a y b es:')
print(f'a + b = {a + b}')

print('El producto de elemento a elemento de a y b es:')
print(f'a * b = {a*b}')

print('El cuadrado de cada elemento de a es:')
print(f'a^2 = {a**2}')

print('La raiz cuadrada de cada elemento de b es:')
print(f'sqrt(b) = {np.sqrt(b)}')

print('La suma de todos los elementos de a es:')
print(f'sum(a) = {np.sum(a)}')