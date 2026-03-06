"""
Módulo para la gestión de tarjetas de vocabulario.

Este módulo define la clase Tarjeta, que representa una palabra con su traducción,
categoría y nivel de dificultad. Permite validar datos, comprobar respuestas del
usuario y comparar tarjetas para evitar duplicados.

Clases:
    - Tarjeta
"""

class Tarjeta:
    """
    dfs
    Clase que representa una tarjeta de vocabulario.

    Atributos:
    palabra: str
        Palabra en el idioma original.
    traduccion: str
        Traducción de la palabra.
    categoria: str
        Categoría temática de la palabra (ej: animales, comida, etc.).
    nivel_dificultad: int
        Nivel de dificultad de la tarjeta.

    Métodos:
    __init__(palabra, traduccion, categoria, nivel_dificultad)
        Inicializa una nueva tarjeta con sus atributos principales.

    es_correcta(respuesta: str) -> bool
        Comprueba si la respuesta dada coincide con la traducción correcta.

    __str__() -> str
        Devuelve una representación legible de la tarjeta.

    __eq__(other) -> bool
        Permite comparar dos tarjetas para comprobar si son iguales.
    """

    def __init__(self, palabra, traduccion, categoria, nivel_dificultad):
        """
        Inicializa una instancia de la clase Tarjeta.

        Parámetros:
        palabra: str
            Palabra en el idioma original.
        traduccion: str
            Traducción correcta de la palabra.
        categoria: str
            Categoría temática de la tarjeta.
        nivel_dificultad: int
            Nivel de dificultad de la palabra.
        """
        self.palabra = palabra
        self.traduccion = traduccion
        self.categoria = categoria
        self.nivel_dificultad = nivel_dificultad

    @property
    def palabra(self):
        """
        Obtiene la palabra almacenada en la tarjeta.
        """
        return self._palabra

    @palabra.setter
    def palabra(self, valor):
        """
        Establece la palabra de la tarjeta validando que no esté vacía.
        """
        if not valor or valor.strip() == "":
            raise ValueError("La palabra no puede estar vacía.")
        self._palabra = valor.strip().lower()

    @property
    def traduccion(self):
        """
        Obtiene la traducción de la palabra.
        """
        return self._traduccion

    @traduccion.setter
    def traduccion(self, valor):
        """
        Establece la traducción validando que no esté vacía.
        """
        if not valor or valor.strip() == "":
            raise ValueError("La traducción no puede estar vacía.")
        self._traduccion = valor.strip().lower()

    def es_correcta(self, respuesta):
        """
        Comprueba si la respuesta proporcionada coincide con la traducción.

        Parámetros:
        -----------
        respuesta: str
            Respuesta dada por el usuario.

        Devuelve:
        --------
        bool
            True si la respuesta es correcta, False en caso contrario.
        """
        if not respuesta or respuesta.strip() == "":
            raise ValueError("La respuesta no puede estar vacía.")
        return respuesta.strip().lower() == self.traduccion

    def __str__(self):
        """
        Devuelve una representación en texto de la tarjeta.

        Devuelve:
        str
            Información básica de la tarjeta.
        """
        return (
            f"Palabra: {self.palabra} | "
            f"Categoría: {self.categoria} | "
            f"Nivel: {self.nivel_dificultad}"
        )

    def __eq__(self, other):
        """
        Compara dos tarjetas para verificar si son iguales.

        Parámetros:
        other: Tarjeta
            Otra tarjeta a comparar.

        Devuelve:
        bool
            True si tienen la misma palabra y traducción.
        """
        if not isinstance(other, Tarjeta):
            return False

        return (
            self.palabra == other.palabra and
            self.traduccion == other.traduccion
        )