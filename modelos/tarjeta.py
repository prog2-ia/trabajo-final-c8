"""Módulo que define la clase Tarjeta."""


class Tarjeta:
    """
    Representa una tarjeta de vocabulario básica.

    Atributos:
        palabra (str): Palabra original.
        traduccion (str): Traducción.
        categoria (str): Categoría temática.
        nivel_dificultad (int): Nivel de dificultad (1-5).
    """

    def __init__(self, palabra: str, traduccion: str,
                 categoria: str, nivel_dificultad: int) -> None:
        """
        Inicializa la tarjeta.

        Parámetros:
            palabra (str): Palabra original.
            traduccion (str): Traducción.
            categoria (str): Categoría.
            nivel_dificultad (int): Nivel entre 1 y 5.
        """
        self.palabra = palabra
        self.traduccion = traduccion
        self.categoria = categoria
        self.nivel_dificultad = nivel_dificultad

    @property
    def palabra(self) -> str:
        """Devuelve la palabra."""
        return self._palabra

    @palabra.setter
    def palabra(self, valor: str) -> None:
        """Establece la palabra validando que no esté vacía."""
        if not valor or valor.strip() == "":
            raise ValueError("La palabra no puede estar vacía.")
        self._palabra = valor.strip().lower()

    @property
    def traduccion(self) -> str:
        """Devuelve la traducción."""
        return self._traduccion

    @traduccion.setter
    def traduccion(self, valor: str) -> None:
        """Establece la traducción validando que no esté vacía."""
        if not valor or valor.strip() == "":
            raise ValueError("La traducción no puede estar vacía.")
        self._traduccion = valor.strip().lower()

    @property
    def nivel_dificultad(self) -> int:
        """Devuelve el nivel de dificultad."""
        return self._nivel_dificultad

    @nivel_dificultad.setter
    def nivel_dificultad(self, valor: int) -> None:
        """Establece el nivel validando que esté entre 1 y 5."""
        if not isinstance(valor, int):
            raise TypeError("El nivel de dificultad debe ser un número entero.")
        if valor < 1 or valor > 5:
            raise ValueError("El nivel de dificultad debe estar entre 1 y 5.")
        self._nivel_dificultad = valor

    def es_correcta(self, respuesta: str) -> bool:
        """
        Comprueba si la respuesta coincide con la traducción.

        Parámetros:
            respuesta (str): Respuesta del usuario.

        Devuelve:
            bool: True si es correcta.

        Lanza:
            ValueError: Si la respuesta está vacía.
        """
        if not respuesta or respuesta.strip() == "":
            raise ValueError("La respuesta no puede estar vacía.")
        return respuesta.strip().lower() == self.traduccion

    def __str__(self) -> str:
        """Representación de la tarjeta."""
        return (
            f"Palabra: {self.palabra} | "
            f"Categoría: {self.categoria} | "
            f"Nivel: {self.nivel_dificultad}"
        )

    def __eq__(self, other: object) -> bool:
        """Compara dos tarjetas por palabra y traducción."""
        if not isinstance(other, Tarjeta):
            return False
        return (
            self.palabra == other.palabra and
            self.traduccion == other.traduccion
        )

    def __hash__(self) -> int:
        """Hash basado en palabra y traducción para uso en sets."""
        return hash((self.palabra, self.traduccion))