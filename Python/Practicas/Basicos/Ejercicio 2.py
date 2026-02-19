import numpy as np  

calificaciones = np.array([55, 78, 82, 90, 61, 74, 88, 95, 70, 63, 77, 85])

print('La media de las calificaciones es:')
print(f'media = {np.mean(calificaciones)}')

print('La mediana de las calificaciones es:')
print(f'mediana = {np.median(calificaciones)}')

print('La desviacion estandar de las calificaciones es:')
print(f'desviacion estandar = {np.std(calificaciones)}')

print('El valor maximo de las calificaciones es:')
print(f'maximo = {np.max(calificaciones)}')

print('El valor minimo de las calificaciones es:')
print(f'minimo = {np.min(calificaciones)}')