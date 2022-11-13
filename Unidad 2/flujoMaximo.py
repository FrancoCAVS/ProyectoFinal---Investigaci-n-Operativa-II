from ortools.graph import pywrapgraph
start_nodes = [0, 0, 0, 1, 1, 2, 2, 3, 3]
end_nodes = [1, 2, 3, 2, 4, 3, 4, 2, 4]
capacities = [20, 30, 10, 40, 30, 10, 20, 5, 20]
max_flow = pywrapgraph.SimpleMaxFlow()
for i in range(0, len(start_nodes)):
    max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])
# Find the maximum flow between node 0 and node 4.
if max_flow.Solve(0, 4) == max_flow.OPTIMAL:
    print('Flujo Maximo:', max_flow.OptimalFlow())
    print('')
    print('  Arco    Flujo / Capacidad')
    for i in range(max_flow.NumArcs()):
        print('%1s -> %1s   %3s  / %3s' % (
          max_flow.Tail(i),
          max_flow.Head(i),
          max_flow.Flow(i),
          max_flow.Capacity(i)))
    print('Corte mínimo del lado de la fuente:', max_flow.GetSourceSideMinCut())
    print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
else:
    print('Hubo un problema con la entrada de flujo máximo.')