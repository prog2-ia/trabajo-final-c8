"""Módulo que define la clase Persistencia."""

import pickle
import os


class Persistencia:
    """
    Gestiona el guardado y carga de datos del sistema.

    Atributos:
        RUTA (str): Archivo donde se almacenan los datos.
    """

    RUTA = "datos.pkl"

    @staticmethod
    def guardar(usuario, mazo):
        """
        Guarda los datos en un archivo.

        Parámetros:
            usuario (Usuario): Usuario a guardar.
            mazo (Mazo): Mazo a guardar.
        """
        with open(Persistencia.RUTA, "wb") as f:
            pickle.dump((usuario, mazo), f)

    @staticmethod
    def cargar():
        """
        Carga los datos si existen.

        Devuelve:
            tuple: (usuario, mazo) o (None, None).
        """
        if not os.path.exists(Persistencia.RUTA):
            return None, None

        with open(Persistencia.RUTA, "rb") as f:
            return pickle.load(f)