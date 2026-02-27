class Tarjeta:
    ''''
    Representa una palabra individual con su traducción, categoría y nivel de dificultad. 
    Permite comprobar si una respuesta es correcta y comparar tarjetas para evitar duplicados. 
    Es la unidad básica del sistema.
    ''''
    def __init__(self, palabra, traduccion, categoria, nivel_dificultad):
        self.palabra=palabra
        self.traduccion=traduccion
        self.categoria=categoria
        self.nivel_dificultad=nivel_dificultad

    def guardar_info(self):

    def es_correcta(self):

    def duplicados(self):

    pass
