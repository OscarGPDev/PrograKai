# Declaracion de un arreglo
mi_arreglo: list[int] = [2, 3, 4, 5]
# Agrega un elemento al arreglo
mi_arreglo.append(2)
print(mi_arreglo)
# Inserta un elemento en la posicion indicada, NO reemplaza al elemento actual, recorre los demas elementos
mi_arreglo.insert(0, 1)
print(mi_arreglo)
# Consulta un elemento al arreglo en una posicion
print(mi_arreglo[2])  # 3
# Reemplazar un valor en una posicion del arreglo
mi_arreglo[5] = 6
print(mi_arreglo[5])  # 6
# Eliminar un elemento del arreglo si lo encuentra, elimina por VALOR, NO por INDICE,
# si no encuentra el elemento lanza un error
mi_arreglo.remove(5)
print(mi_arreglo)
# Saber si un elemento se encuentra en un arreglo
print(6 in mi_arreglo)  # True
print(5 in mi_arreglo)  # False
# Saber el tamanio de un arreglo
print(len(mi_arreglo))
