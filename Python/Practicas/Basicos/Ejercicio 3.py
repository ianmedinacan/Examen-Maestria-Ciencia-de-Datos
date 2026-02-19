import numpy as np

A = np.array([[1, 2, 3],   
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print('La suma de las matrices A y B es:')
print(f'A + B = {A + B}')
print('\n')
print('La multiplicacion matricial de las matrices A y B es:')
print(f'A X B = {A@B}')
print('\n')
print('La transpuesta de la matriz A es:')
print(f'A^T = {A.T}')
print('\n')
print('El determinante de la matriz A es:')
print(f'det(A) = {np.linalg.det(A)}')
print('\n')
print('La traza de la matriz A es:')
print(f'trace(A) = {np.trace(A)}')
