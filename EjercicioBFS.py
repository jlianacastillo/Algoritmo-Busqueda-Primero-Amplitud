# Desarrollado por Brayan Baquero y Juliana Castillo
# Asignatura de Inteligencia Artificial 
# Profesor : Manuel Alexander Cadena 
# Universidad de Cundinamarca
# Ingenieria de Sistemas


import os
from collections import deque
cola = deque()
print(cola)
deque([])
visitados = []

grafo = {"a": [("d", 1), ("f", 2), ("g", 3)],

         "d": [("a", 1), ("h", 4), ("c", 5)],
         "f": [("a", 2), ("h", 6), ("i", 7)],
         "g": [("a", 3)],

         "h": [("d", 4), ("k", 8)],
         "c": [("d", 5), ("j", 9)],
         "b": [("f", 6), ("l", 8)],
         "i": [("f", 7), ("m", 7), ("c", 6)],

         "k": [("h", 8), ],
         "j": [("c", 9), ("x", 10)],
         "l": [("b", 6), ("z", 11)],
         "m": [("i", 7)],
         "n": [("i", 4)],

         "x": [("j", 10)],
         "z": [("l", 11)],

         }

print("Muestra el grafo antes del recorrido: \n")

for key, list in grafo.items():

    print(key)
    print(list)

origen = input("ingresar Nodo Origen :")
print("lista de recorrido de amplitud ")

cola.append(origen)
while cola:
    actual = cola.popleft()
    if actual not in visitados:
        print("vetice actual =", actual)
        visitados.append(actual)

        for key, list in grafo[actual]:
            if key not in visitados:
                cola.append(key)
