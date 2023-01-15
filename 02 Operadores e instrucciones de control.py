def bucle_for(arreglo: list) -> None:
    for elemento in arreglo:
        print(elemento)


def bucle_while(arreglo: list) -> None:
    tamanio_arreglo: int = len(arreglo)
    iterador: int = 0
    while iterador < tamanio_arreglo:
        print(arreglo[iterador])
        iterador += 1


def condicional(parametro1, parametro2) -> None:
    if parametro1 == parametro2:
        print("Los parametros son iguales")
    elif parametro1 != parametro2 and type(parametro1) == type(parametro2):
        print("Los parametros son diferentes pero son del mismo tipo")
    else:
        print("Los parametros son diferentes y de diferente tipo")


def operadores() -> None:
    variable: int = 100
    # operadores de asignacion
    variable + 5
    variable - 5
    variable / 5
    variable % 5
    variable * 5
    # operadores de asignacion
    variable += 1  # variable = variable + 1
    variable -= 1  # variable = variable - 1
    variable /= 1  # variable = variable / 1
    variable %= 1  # variable = variable % 1
    variable *= 1  # variable = variable * 1
    # operadores logicos
    variable_logica: bool = False
    otra_variable_logica: bool = False
    variable_logica == otra_variable_logica
    variable_logica != otra_variable_logica
    variable_logica and otra_variable_logica
    variable_logica or otra_variable_logica
    not variable_logica
