#Importar las librerías necesarias
from criticalpath import Node
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np


#Ingresar los datos del modelo (Tareas y dependencias)
#Crear el proyecto "p"
p = Node('proyecto')

tareas = [("A", {"duracion": 3}), 
          ("B", {"duracion": 2}), 
          ("C", {"duracion": 4}), 
          ("D", {"duracion": 3}), 
          ("E", {"duracion": 2}), 
          ("F", {"duracion": 4}), 
          ("G", {"duracion": 2}), 
          ("H", {"duracion": 1}), 
          ("I", {"duracion": 2}), 
          ("J", {"duracion": 4})]

dependencias = [("A", "E"), 
                ("B", "E"), 
                ("E", "F"),
                ("F", "G"), 
                ("G", "I"), 
                ("I", "J"),
                ("C", "J"), 
                ("H", "I"), 
                ("D", "H")]

# Cargar al proyecto las tareas y sus duraciones
for i in tareas:
    p.add(Node(i[0], duration=i[1]["duracion"]))

# Cargar al proyecto sus dependencias (secuencias)
for j in dependencias:
    p.link(j[0],j[1])

# Actualizar el proyecto:
p.update_all()

#Obtener la Ruta Crítica del modelo
variable=p.get_critical_path()
print("Ruta Crítica del modelo es:",variable)

#Obtener la duración del proyecto
tiempo=p.duration
print("La duracion es:", tiempo)