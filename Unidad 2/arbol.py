class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        #Inicializar la matriz de adyacencia con ceros
        self.m_graph = [[0 for column in range(num_of_nodes)] 
                    for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight):
        self.m_graph[node1][node2] = weight
        self.m_graph[node2][node1] = weight

def prims_mst(self):
    #Definir un número realmente grande, siempre tendrá el peso más alto en las comparaciones.
    postitive_inf = float('inf')

    #Esta es una lista que muestra qué nodos ya están seleccionados
    #Para que no elijamos el mismo nodo dos veces y podamos saber cuándo dejar de buscar
    selected_nodes = [False for node in range(self.m_num_of_nodes)]

    # Matriz del MST resultante
    result = [[0 for column in range(self.m_num_of_nodes)] 
                for row in range(self.m_num_of_nodes)]
    
    indx = 0
    for i in range(self.m_num_of_nodes):
        print(self.m_graph[i])
    
    print(selected_nodes)

    #Si bien hay nodos que no están incluidos en el MST, siga buscando:
    while(False in selected_nodes):
        #Usamos el número grande que creamos antes como el peso mínimo posible
        minimum = postitive_inf

        # El nodo inicial
        start = 0

        # El nodo final
        end = 0

        for i in range(self.m_num_of_nodes):
            # Si el nodo es parte del MST, mira sus relaciones
            if selected_nodes[i]:
                for j in range(self.m_num_of_nodes):
                    #Si el nodo analizado tiene una ruta al nodo final Y no está incluido en el MST (para evitar ciclos)
                    if (not selected_nodes[j] and self.m_graph[i][j]>0):  
                        #Si la ruta de peso analizada es menor que el mínimo del MST
                        if self.m_graph[i][j] < minimum:
                            # Define el nuevo peso mínimo, el vértice inicial y el vértice final
                            minimum = self.m_graph[i][j]
                            start, end = i, j
        
        # Como agregamos el vértice final al MST, ya está seleccionado:
        selected_nodes[end] = True

        # Llenar los campos de la matriz de adyacencia MST:
        result[start][end] = minimum
        
        if minimum == postitive_inf:
            result[start][end] = 0

        print("(%d.) %d - %d: %d" % (indx, start, end, result[start][end]))
        indx += 1
        
        result[end][start] = result[start][end]

    # Imprima el MST resultante
    for i in range(len(result)):
        for j in range(0+i, len(result)):
            if result[i][j] != 0:
                print("%d - %d: %d" % (i, j, result[i][j]))

#El gráfico de ejemplo tiene 9 nodos.
example_graph = Graph(9)

example_graph.add_edge(0, 1, 4)
example_graph.add_edge(0, 2, 7)
example_graph.add_edge(1, 2, 11)
example_graph.add_edge(1, 3, 9)
example_graph.add_edge(1, 5, 20)
example_graph.add_edge(2, 5, 1)
example_graph.add_edge(3, 6, 6)
example_graph.add_edge(3, 4, 2)
example_graph.add_edge(4, 6, 10)
example_graph.add_edge(4, 8, 15)
example_graph.add_edge(4, 7, 5)
example_graph.add_edge(4, 5, 1)
example_graph.add_edge(5, 7, 3)
example_graph.add_edge(6, 8, 5)
example_graph.add_edge(7, 8, 12)

example_graph.prims_mst()