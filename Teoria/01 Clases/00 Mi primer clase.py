"""
Una clase es un modelo que usamos para describir una entidad mediante atributos y metodos,
los atributos denotan datos que son relevantes para nosotros de una entidad, y los metodos
acciones que se realizan con los datos de la entidad o que esta realiza sobre otros.
"""


class MiClase():
    # Atributo
    mi_atributo: str = "Soy un atributo de una clase"

    def metodo(self, parametro="soy el valor por default del parametro"):
        """ Metodo
    self, es un nombre de argumento reservado, que se indica para decir que un metodo
    interactuara con la entidad, es opcional ponerlo, a menos de que uses un
    atributo que pertenece a la clase, como es el caso de 'mi_atributo', no obstante
    'self' se coloca UNICAMENTE en la firma de la funcion, cuando se llama simplemente
    es nombre_objeto.metodo(parametro)
    """
        print(f"Soy un metodo de una clase, recibi el parametro con valor: {str(parametro)}")
        print(f"Mi clase tiene un atributo llamado 'mi atributo' con el valor: {self.mi_atributo}")

    def __init__(self, parametro=None):
        """
        Constructor
        Es un metodo especial que se utiliza para inicializar un objeto de una clase
        puede recibir argumentos, pero en general solo debe usarse para inicializar
        los atributos escenciales
        """
        print("Soy un constructor de una clase")
        if parametro:
            self.mi_atributo = parametro


mi_objeto = MiClase()
mi_objeto.metodo("soy un parametro")
