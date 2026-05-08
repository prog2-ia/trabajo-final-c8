"""Módulo para la gestión de mazos.

Este módulo define la clase GestorMazos, encargada de gestionar uno o varios
mazos de tarjetas. Permite crear, añadir, obtener y eliminar mazos.

Clases:
    - GestorMazos
"""

from modelos.mazo import Mazo


class GestorMazos:
    """
    Clase encargada de gestionar uno o varios mazos.

    Atributos:
    _mazos: list[Mazo]
        Lista interna que almacena los mazos gestionados.

    Métodos:
    __init__() -> None
        Inicializa el gestor con una lista vacía de mazos.

    crear_mazo(nombre: str) -> Mazo
        Crea un nuevo mazo con el nombre indicado y lo añade al gestor.

    anadir_mazo(mazo: Mazo) -> None
        Añade un mazo existente al gestor.

    obtener_mazos() -> list[Mazo]
        Devuelve la lista de mazos gestionados.

    obtener_mazo(nombre: str) -> Mazo | None
        Devuelve un mazo por su nombre si existe.

    eliminar_mazo(nombre: str) -> None
        Elimina un mazo del gestor a partir de su nombre.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase GestorMazos.
        """
        self._mazos = []

    def crear_mazo(self, nombre):
        """
        Crea un nuevo mazo y lo añade al gestor.

        Parámetros:
        nombre: str
            Nombre del mazo.

        Devuelve:
        Mazo
            El mazo creado.
        """
        mazo = Mazo(nombre)
        self._mazos.append(mazo)
        return mazo

    def anadir_mazo(self, mazo):
        """
        Añade un mazo existente al gestor.

        Parámetros:
        mazo: Mazo
            Mazo que se desea añadir.

        Lanza:
        TypeError
            Si el objeto no es de tipo Mazo.
        """
        if not isinstance(mazo, Mazo):
            raise TypeError("Debe ser un objeto Mazo")

        self._mazos.append(mazo)

    def obtener_mazos(self):
        """
        Devuelve la lista de mazos gestionados.

        Devuelve:
        list[Mazo]
            Lista de mazos.
        """
        return self._mazos

    def obtener_mazo(self, nombre):
        """
        Busca un mazo por su nombre.

        Parámetros:
        nombre: str
            Nombre del mazo.

        Devuelve:
        Mazo | None
            El mazo si existe, o None en caso contrario.
        """
        for mazo in self._mazos:
            if mazo.nombre == nombre:
                return mazo
        return None

    def eliminar_mazo(self, nombre):
        """
        Elimina un mazo del gestor.

        Parámetros:
        nombre: str
            Nombre del mazo a eliminar.
        """
        mazo = self.obtener_mazo(nombre)
        if mazo:
            self._mazos.remove(mazo)