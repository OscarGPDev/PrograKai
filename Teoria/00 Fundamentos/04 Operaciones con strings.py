# Declaracion de un string
mi_string: str = "String de prueba"
# Concatenacion de un string
mi_string = mi_string + ", concatenado" + " con dos strings"
print(mi_string)
mi_string += "concatenado con operador de asignacion"
print(mi_string)
# repetir un string
mi_string = mi_string * 2
print(mi_string)
# Separar un string a arreglo con un caracter
print(mi_string.split(","))
# Saber si un string se encuentra dentro de otro
print("prueba" in mi_string)
# Convertir a mayusculas
print(mi_string.upper())
# Convertir a minusculas
print(mi_string.lower())
# Referencia completa en https://docs.python.org/es/3/library/string.html
# Mas ejemplos en https://www.w3schools.com/python/python_strings.asp
