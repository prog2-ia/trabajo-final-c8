"""Módulo para la persistencia de datos del sistema.

Este módulo define la clase Persistencia, encargada de guardar y cargar
los datos del usuario y el mazo en un archivo utilizando serialización
con pickle.

Clases:
    - Persistencia
"""

import pickle
import os

class Persistencia:
    """
    Clase encargada de gestionar la persistencia de datos.

    Permite guardar y cargar el estado del usuario y del mazo en un archivo
    para mantener la información entre ejecuciones del programa.

    Atributos:
    ----------
    RUTA: str
        Ruta del archivo donde se almacenan los datos serializados.

    Métodos:
    -------
    guardar(usuario, mazo) -> None
        Guarda el usuario y el mazo en un archivo.

    cargar() -> tuple[Usuario | None, Mazo | None]
        Carga el usuario y el mazo desde el archivo si existe.
    """

    RUTA = "datos.pkl"

    @staticmethod
    def guardar(usuario, mazo):
        """
        Guarda el usuario y el mazo en un archivo.

        Parámetros:
        ----------
        usuario: Usuario
            Objeto usuario que se desea guardar.
        mazo: Mazo
            Objeto mazo que se desea guardar.
        """
        with open(Persistencia.RUTA, "wb") as f:
            pickle.dump((usuario, mazo), f)

    @staticmethod
    def cargar():
        """
        Carga el usuario y el mazo si existen en el archivo.

        Devuelve:
        --------
        tuple
            Una tupla (usuario, mazo) si el archivo existe,
            o (None, None) si no hay datos guardados.
        """
        if not os.path.exists(Persistencia.RUTA):
            return None, None

        with open(Persistencia.RUTA, "rb") as f:
            return pickle.load(f)