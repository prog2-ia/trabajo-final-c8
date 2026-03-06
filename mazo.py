"""
Módulo para la gestión de mazos de tarjetas.

Este módulo define la clase Mazo, que representa un conjunto de tarjetas
organizadas bajo un mismo nombre o temática. Permite añadir, eliminar,
mezclar tarjetas y combinar mazos mediante sobrecarga de operadores.

Clases:
    - Mazo
"""

from tarjeta import Tarjeta
import random

class Mazo:
    """
    Clase que representa un conjunto de tarjetas.

    Atributos:
    nombre: str
        Nombre del mazo o temática que agrupa las tarjetas.
    _tarjetas: list[Tarjeta]
        Lista interna que almacena las tarjetas del mazo.

    Métodos:
    __init__(nombre: str) -> None
        Inicializa un nuevo mazo con un nombre.

    anadir_tarjeta(tarjeta: Tarjeta) -> None
        Añade una nueva tarjeta al mazo si no está duplicada.

    eliminar_tarjeta(tarjeta: Tarjeta) -> None
        Elimina una tarjeta existente del mazo.

    mezclar_tarjetas() -> None
        Mezcla aleatoriamente el orden de las tarjetas del mazo.

    __add__(other: Mazo) -> Mazo
        Permite unir dos mazos creando uno nuevo con las tarjetas de ambos.

    __eq__(other: Mazo) -> bool
        Permite comparar dos mazos comprobando si contienen las mismas tarjetas.

    __len__() -> int
        Devuelve el número de tarjetas que contiene el mazo.

    __str__() -> str
        Devuelve una representación del mazo.
    """

    def __init__(self, nombre):
        """
        Inicializa una instancia de la clase Mazo.

        Parámetros:
        nombre: str
            Nombre que identifica el mazo.
        """
        self.nombre = nombre
        self._tarjetas = []

    @property
    def nombre(self):
        """
        Obtiene el nombre del mazo.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """
        Establece el nombre del mazo validando que no esté vacío.
        """
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    @property
    def tarjetas(self):
        """
        Devuelve una copia de la lista de tarjetas del mazo.
        Se devuelve una copia para evitar modificar la lista directamente.
        """
        return self._tarjetas.copy()

    def anadir_tarjeta(self, tarjeta):
        """
        Añade una tarjeta al mazo.

        Parámetros:
        tarjeta: Tarjeta
            Tarjeta que se desea añadir.

        Lanza:
        TypeError
            Si el objeto no es una Tarjeta.
        ValueError
            Si la tarjeta ya existe en el mazo.
        """
        if not isinstance(tarjeta, Tarjeta):
            raise TypeError("El objeto debe ser de tipo Tarjeta")

        if tarjeta in self._tarjetas:
            raise ValueError("La tarjeta ya existe en el mazo")

        self._tarjetas.append(tarjeta)

    def eliminar_tarjeta(self, tarjeta):
        """
        Elimina una tarjeta del mazo.

        Parámetros:
        tarjeta: Tarjeta
            Tarjeta que se desea eliminar.

        Lanza:
        ValueError
            Si la tarjeta no se encuentra en el mazo.
        """
        if tarjeta not in self._tarjetas:
            raise ValueError("La tarjeta no está en el mazo")

        self._tarjetas.remove(tarjeta)

    def mezclar_tarjetas(self):
        """
        Mezcla aleatoriamente el orden de las tarjetas del mazo.
        """
        random.shuffle(self._tarjetas)

    def __add__(self, other):
        """
        Une dos mazos creando uno nuevo.

        Parámetros:
        other: Mazo
            Mazo que se desea combinar con el actual.

        Retorna:
        Mazo
            Nuevo mazo que contiene las tarjetas de ambos mazos sin duplicados.
        """
        if not isinstance(other, Mazo):
            raise TypeError("Solo se pueden unir objetos de tipo Mazo")

        nuevo_mazo = Mazo(f"{self.nombre} + {other.nombre}")

        for tarjeta in self._tarjetas:
            nuevo_mazo.anadir_tarjeta(tarjeta)

        for tarjeta in other._tarjetas:
            if tarjeta not in nuevo_mazo._tarjetas:
                nuevo_mazo.anadir_tarjeta(tarjeta)

        return nuevo_mazo

    def __eq__(self, other):
        """
        Compara dos mazos para comprobar si contienen las mismas tarjetas.

        Parámetros:
        other: Mazo
            Mazo con el que se quiere comparar.

        Retorna:
        bool
            True si ambos mazos contienen las mismas tarjetas.
        """
        if not isinstance(other, Mazo):
            return False

        if len(self._tarjetas) != len(other._tarjetas):
            return False

        for tarjeta in self._tarjetas:
            if tarjeta not in other._tarjetas:
                return False

        return True

    def __len__(self):
        """
        Devuelve el número de tarjetas del mazo.
        """
        return len(self._tarjetas)

    def __str__(self):
        """
        Devuelve una representación del mazo.

        Retorna:
        str
            Nombre del mazo y número de tarjetas que contiene.
        """
        return (
            f"Mazo: {self.nombre}\n"
            f"Número de tarjetas: {len(self)}"
        )