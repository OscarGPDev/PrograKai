# De esta forma definimos una funcion
def saluda():
    nombre = input("Introduce tu nombre\n")
    print(f"Hola {nombre}")


# De esta forma indicamos un parametro, en python no es necesario indicar explicitamente el tipo de dato
def imprime_parametro(parametro):
    print(f"El tipo de parametro es: {type(parametro)}")
    print(parametro)


def funcion_con_tipos(parametro: bool) -> bool:
    """
    Esta funcion regresa el mismo parametro que se le provee
    parametro : bool
        parametro booleano que regresara la funcion
    """
    variable_tipada: bool = parametro
    variable_arreglo: list[int] = [1, 2, 3, 4]
    return parametro


imprime_parametro("Soy un string")
imprime_parametro(1)
imprime_parametro(1.2)
imprime_parametro(False)
imprime_parametro([])
imprime_parametro(None)
imprime_parametro(lambda x: print(x))

# Convertir entre tipos
str(100)  # convierte a string
int("30")  # convierte a int
float("10.3")  # convierte a float
