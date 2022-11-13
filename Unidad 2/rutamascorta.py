from __future__ import print_function
from ortools.graph import pywrapgraph

def main():
  """MinCostFlow adaptado a la ruta más corta - interfaz de ejemplo."""

  # Define cuatro matrices paralelas: nodos_fuente, nodos_destino, 
  # capacidades, y costos_unitarios entre cada par.

  nodos_fuente      = [ 0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7]
  nodos_destino     = [ 1, 2, 2, 3, 1, 3, 4, 5, 6, 3, 6, 7, 6, 8, 5, 7, 8, 6, 8]
  capacidades       = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  distancia         = [ 4, 2, 2, 7, 4, 9, 6, 1, 5, 2, 3, 2, 1, 5, 4, 3, 6, 2, 6]

  # Define una matriz con los suministros de cada nodo (valores positivos = 
  # suministros) y (valores negativos = demandas)

  suministros = [1, 0, 0, 0, 0, 0, 0, 0, -1]


  # Crea una instancia para el solucionador
  min_cost_flow = pywrapgraph.SimpleMinCostFlow()

  # Define cada arco del problema
  for i in range(0, len(nodos_fuente)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(nodos_fuente[i], nodos_destino[i],
                                                capacidades[i], distancia[i])

  # Define los suministros para cada nodo.

  for i in range(0, len(suministros)):
    min_cost_flow.SetNodeSupply(i, suministros[i])


  # Encuentra el costo mínimo entre el nodo 0 y el nodo 8
  if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Distancia mínima:', min_cost_flow.OptimalCost())
    print('')
    print('  Arco    Flujo / Capacidad  Distancia')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      print('%1s -> %1s    %3s   / %3s       %3s' % (
          min_cost_flow.Tail(i),
          min_cost_flow.Head(i),
          min_cost_flow.Flow(i),
          min_cost_flow.Capacity(i),
          cost))
  else:
    print('Hubo un problema con la entrada de flujo de distancia mínima.')

if __name__ == '__main__':
  main()
