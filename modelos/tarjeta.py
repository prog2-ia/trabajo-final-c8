"""Módulo que define la clase Tarjeta."""

class Tarjeta:
    """
    Representa una tarjeta de vocabulario.

    Atributos:
        palabra (str): Palabra original.
        traduccion (str): Traducción.
        categoria (str): Categoría temática.
        nivel_dificultad (int): Nivel de dificultad.
    """

    def __init__(self, palabra, traduccion, categoria, nivel_dificultad):
        """
        Inicializa la tarjeta.

        Parámetros:
            palabra (str): Palabra original.
            traduccion (str): Traducción.
            categoria (str): Categoría.
            nivel_dificultad (int): Nivel de dificultad.
        """
        self.palabra = palabra
        self.traduccion = traduccion
        self.categoria = categoria
        self.nivel_dificultad = nivel_dificultad

    @property
    def palabra(self):
        """Devuelve la palabra."""
        return self._palabra

    @palabra.setter
    def palabra(self, valor):
        """Establece la palabra validando que no esté vacía."""
        if not valor or valor.strip() == "":
            raise ValueError("La palabra no puede estar vacía.")
        self._palabra = valor.strip().lower()

    @property
    def traduccion(self):
        """Devuelve la traducción."""
        return self._traduccion

    @traduccion.setter
    def traduccion(self, valor):
        """Establece la traducción validando que no esté vacía."""
        if not valor or valor.strip() == "":
            raise ValueError("La traducción no puede estar vacía.")
        self._traduccion = valor.strip().lower()

    def es_correcta(self, respuesta):
        """
        Comprueba si la respuesta coincide con la traducción.

        Parámetros:
            respuesta (str): Respuesta del usuario.

        Devuelve:
            bool: True si es correcta.
        """
        if not respuesta or respuesta.strip() == "":
            raise ValueError("La respuesta no puede estar vacía.")
        return respuesta.strip().lower() == self.traduccion

    def __str__(self):
        """Representación de la tarjeta."""
        return (
            f"Palabra: {self.palabra} | "
            f"Categoría: {self.categoria} | "
            f"Nivel: {self.nivel_dificultad}"
        )

    def __eq__(self, other):
        """
        Compara dos tarjetas.

        Devuelve:
            bool: True si tienen misma palabra y traducción.
        """
        if not isinstance(other, Tarjeta):
            return False
        return (
            self.palabra == other.palabra and
            self.traduccion == other.traduccion
        )