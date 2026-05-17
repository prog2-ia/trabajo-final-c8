"""Módulo que define la clase MazoPorNivel."""

from modelos.mazo import Mazo
from modelos.tarjeta import Tarjeta


class MazoPorNivel(Mazo):
    """
    Mazo que solo acepta tarjetas de un nivel de dificultad concreto.

    Hereda de Mazo y restringe las tarjetas al nivel indicado.

    Atributos:
        nivel (int): Nivel de dificultad permitido (1-5).
    """

    def __init__(self, nombre: str, nivel: int) -> None:
        """
        Inicializa el mazo por nivel.

        Parámetros:
            nombre (str): Nombre del mazo.
            nivel (int): Nivel de dificultad permitido (1-5).

        Lanza:
            TypeError: Si nivel no es entero.
            ValueError: Si nivel no está entre 1 y 5.
        """
        super().__init__(nombre)
        if not isinstance(nivel, int):
            raise TypeError("El nivel debe ser un número entero.")
        if nivel < 1 or nivel > 5:
            raise ValueError("El nivel debe estar entre 1 y 5.")
        self._nivel = nivel

    @property
    def nivel(self) -> int:
        """Devuelve el nivel permitido."""
        return self._nivel

    def anadir_tarjeta(self, tarjeta: Tarjeta) -> None:
        """
        Añade una tarjeta solo si su nivel coincide con el del mazo.

        Parámetros:
            tarjeta (Tarjeta): Tarjeta a añadir.

        Lanza:
            TypeError: Si no es una Tarjeta.
            ValueError: Si el nivel de la tarjeta no coincide,
                        o si ya existe en el mazo.
        """
        if not isinstance(tarjeta, Tarjeta):
            raise TypeError("El objeto debe ser de tipo Tarjeta.")
        if tarjeta.nivel_dificultad != self._nivel:
            raise ValueError(
                f"Esta tarjeta es de nivel {tarjeta.nivel_dificultad}, "
                f"pero este mazo solo acepta nivel {self._nivel}."
            )
        super().anadir_tarjeta(tarjeta)

    def __str__(self) -> str:
        """Representación del mazo por nivel."""
        return (
            f"Mazo Nivel {self._nivel}: {self.nombre}\n"
            f"Tarjetas: {len(self)}"
        )