#Algoritmo de minimax

matrix = [[-3, -2, 6], [2, 0, 2], [5, -2, -4]]

minimo = list(map(min, matrix))
maximin = max(minimo)
print('Maximin: ', maximin)

transpose = list(zip(*matrix))
maximo = list(map(max, transpose))
minimax = min(maximo)
print('Maximin: ', minimax)

# Extremo
print('Maximin', max(list(map(min, matrix))))
print('Minimax', min(list(map(max, list(zip(*matrix))))))