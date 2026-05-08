"""Módulo que define la clase GestorMazos."""

from modelos.mazo import Mazo


class GestorMazos:
    """
    Gestiona uno o varios mazos de tarjetas.

    Atributos:
        _mazos (list[Mazo]): Lista de mazos.
    """

    def __init__(self):
        """Inicializa el gestor."""
        self._mazos = []

    def crear_mazo(self, nombre):
        """
        Crea un nuevo mazo.

        Parámetros:
            nombre (str): Nombre del mazo.

        Devuelve:
            Mazo: Mazo creado.
        """
        mazo = Mazo(nombre)
        self._mazos.append(mazo)
        return mazo

    def anadir_mazo(self, mazo):
        """
        Añade un mazo existente.

        Parámetros:
            mazo (Mazo): Mazo a añadir.
        """
        if not isinstance(mazo, Mazo):
            raise TypeError("Debe ser un objeto Mazo")
        self._mazos.append(mazo)

    def obtener_mazos(self):
        """
        Devuelve todos los mazos.

        Devuelve:
            list[Mazo]: Lista de mazos.
        """
        return self._mazos

    def obtener_mazo(self, nombre):
        """
        Busca un mazo por nombre.

        Parámetros:
            nombre (str): Nombre del mazo.

        Devuelve:
            Mazo | None: Mazo encontrado o None.
        """
        for mazo in self._mazos:
            if mazo.nombre == nombre:
                return mazo
        return None

    def eliminar_mazo(self, nombre):
        """
        Elimina un mazo por nombre.

        Parámetros:
            nombre (str): Nombre del mazo.
        """
        mazo = self.obtener_mazo(nombre)
        if mazo:
            self._mazos.remove(mazo)