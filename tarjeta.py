class Tarjeta:
    """
    Representa una palabra individual con su traducción, categoría y nivel de dificultad.
    Permite comprobar si una respuesta es correcta y comparar tarjetas para evitar duplicados.
    Es la unidad básica del sistema.
    """

    def __init__(self, palabra, traduccion, categoria, nivel_dificultad):
        self.palabra = palabra
        self.traduccion = traduccion
        self.categoria = categoria
        self.nivel_dificultad = nivel_dificultad


    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("La palabra no puede estar vacía.")
        self._palabra = valor.strip().lower()


    @property
    def traduccion(self):
        return self._traduccion

    @traduccion.setter
    def traduccion(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("La traducción no puede estar vacía.")
        self._traduccion = valor.strip().lower()



    def es_correcta(self, respuesta):
        if not respuesta or respuesta.strip() == "":
            raise ValueError("La respuesta no puede estar vacía.")
        return respuesta.strip().lower() == self.traduccion



    def __str__(self):
        return (f"Palabra: {self.palabra} | "
                f"Categoría: {self.categoria} | "
                f"Nivel: {self.nivel_dificultad}")

    def __eq__(self, other):
        if not isinstance(other, Tarjeta):
            return False
        return (self.palabra == other.palabra and
                self.traduccion == other.traduccion)