from array import array
import numpy as np
import nashpy as nash
# Crear la matriz de pagos
A = np.array([[4, 0], [0, 2]])  # A es el jugador de fila
B = np.array([[2, 0], [0, 4]])  # B Es el jugador de columna
game2 = nash.Game(A, B)
game2
#Encuentre el equilibrio de Nash con enumeración de soporte
getEquilibrium= lambda: game2.support_enumeration()


print("3 lineas de salida")
# Jugador A tiene estrategias de arriba hacia abajo, Jugador B de izq a derecha
# los dos primeros son los equilbirios de nash pero proque sucede una tercera linea? Porque es un equilibrio de Nash con estrategia mixta
eq = getEquilibrium()
for item in eq:
    print(item)


eq = getEquilibrium()
sigma_r, sigma_c = [array for array in eq][-1]
pd = nash.Game(A, B)

print("punto de equilibrio con estrategias mixtas")
print(pd[sigma_r, sigma_c])