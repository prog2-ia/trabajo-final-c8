from tarjeta import Tarjeta

class Ejercicio:
    '''
    Es la clase base que representa una actividad de práctica asociada a una tarjeta. Define la estructura común de todos los tipos de ejercicio, incluyendo cómo mostrar el enunciado y comprobar respuestas. Permite aplicar herencia y polimorfismo.
    '''
    def __init__(self, tarjeta, puntuacion):