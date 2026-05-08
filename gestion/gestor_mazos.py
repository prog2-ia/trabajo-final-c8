from modelos.mazo import Mazo

class GestorMazos:
    """
    Clase encargada de gestionar uno o varios mazos.
    """

    def __init__(self):
        self._mazos = []

    def crear_mazo(self, nombre):
        mazo = Mazo(nombre)
        self._mazos.append(mazo)
        return mazo

    def anadir_mazo(self, mazo):
        if not isinstance(mazo, Mazo):
            raise TypeError("Debe ser un objeto Mazo")
        self._mazos.append(mazo)

    def obtener_mazos(self):
        return self._mazos

    def obtener_mazo(self, nombre):
        for mazo in self._mazos:
            if mazo.nombre == nombre:
                return mazo
        return None

    def eliminar_mazo(self, nombre):
        mazo = self.obtener_mazo(nombre)
        if mazo:
            self._mazos.remove(mazo)