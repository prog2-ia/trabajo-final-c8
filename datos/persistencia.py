import pickle
import os

class Persistencia:
        RUTA = "datos.pkl"

        @staticmethod
        def guardar(usuario, mazo):
            """
            Guarda el usuario y el mazo en un archivo.
            """
            with open(Persistencia.RUTA, "wb") as f:
                pickle.dump((usuario, mazo), f)

        @staticmethod
        def cargar():
            """
            Carga el usuario y el mazo si existen.
            """
            if not os.path.exists(Persistencia.RUTA):
                return None, None

            with open(Persistencia.RUTA, "rb") as f:
                return pickle.load(f)