"""Módulo que define la clase TarjetaAvanzada."""

from modelos.tarjeta import Tarjeta


class TarjetaAvanzada(Tarjeta):
    """
    Tarjeta de vocabulario avanzada que incluye una oración de ejemplo.

    Hereda de Tarjeta y añade el atributo ejemplo.

    Atributos:
        ejemplo (str): Oración de ejemplo usando la palabra.
    """

    def __init__(self, palabra: str, traduccion: str,
                 categoria: str, nivel_dificultad: int, ejemplo: str) -> None:
        """
        Inicializa la tarjeta avanzada.

        Parámetros:
            palabra (str): Palabra original.
            traduccion (str): Traducción.
            categoria (str): Categoría.
            nivel_dificultad (int): Nivel entre 1 y 5.
            ejemplo (str): Oración de ejemplo.
        """
        super().__init__(palabra, traduccion, categoria, nivel_dificultad)
        self.ejemplo = ejemplo

    @property
    def ejemplo(self) -> str:
        """Devuelve el ejemplo."""
        return self._ejemplo

    @ejemplo.setter
    def ejemplo(self, valor: str) -> None:
        """Establece el ejemplo validando que no esté vacío."""
        if not valor or valor.strip() == "":
            raise ValueError("El ejemplo no puede estar vacío.")
        self._ejemplo = valor.strip()

    def mostrar_ejemplo(self) -> str:
        """
        Devuelve la tarjeta con su oración de ejemplo.

        Devuelve:
            str: Representación con ejemplo.
        """
        return f"{super().__str__()} | Ejemplo: {self.ejemplo}"

    def __str__(self) -> str:
        """Representación extendida con el ejemplo."""
        return (
            f"Palabra: {self.palabra} | "
            f"Categoría: {self.categoria} | "
            f"Nivel: {self.nivel_dificultad} | "
            f"Ejemplo: {self.ejemplo}"
        )