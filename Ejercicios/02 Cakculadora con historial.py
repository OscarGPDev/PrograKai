"""
Termina de implementar la siguiente calculadora, puedes modificar el codigo provisto
"""
historial: list[str] = []


def suma(a: float, b: float) -> float:
    historial.append(f"{a} + {b}")
    resultado = a + b
    print(resultado)
    return resultado


def menu():
    while True:
        print("""Ingresa el numero de la operacion a realizar
            1) Suma
            2) Resta
            3) Multiplicacion
            4) Division
            5) Imprimir historial
            6) Salir
        """)
        opcion = input()
        if not opcion.isdigit():
            print("Elige una opcion valida")
        else:
            opcion = int(opcion)
        if opcion == 6:
            break
        elif opcion >= 6 and opcion <= 0:
            print("Elige una opcion valida")
            continue
        elif opcion == 5:
            print(historial)
            continue
        primer_operando = float(input("Ingresa el primer operando: "))
        segundo_operando = float(input("Ingresa el primer operando: "))
        if opcion == 1:
            suma(primer_operando, segundo_operando)


menu()
