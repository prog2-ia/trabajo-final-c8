class Usuario:

    def __init__(self, nombre, puntuacion=0, num_ejercicios=0, num_aciertos=0):
        self.nombre = nombre
        self.puntuacion = puntuacion
        self.num_ejercicios = num_ejercicios
        self.num_aciertos = num_aciertos


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, valor):
        if not isinstance(valor, int):
            raise TypeError("La puntuación debe ser un número entero")
        if valor < 0:
            raise ValueError("La puntuación no puede ser negativa")
        self._puntuacion = valor

    @property
    def num_ejercicios(self):
        return self._num_ejercicios

    @num_ejercicios.setter
    def num_ejercicios(self, valor):
        if valor < 0:
            raise ValueError("El número de ejercicios no puede ser negativo")
        self._num_ejercicios = valor

    @property
    def num_aciertos(self):
        return self._num_aciertos

    @num_aciertos.setter
    def num_aciertos(self, valor):
        if valor < 0:
            raise ValueError("El número de aciertos no puede ser negativo")
        self._num_aciertos = valor


    def actualizar_progreso(self, correcto, puntos):

        self.num_ejercicios += 1

        if correcto:
            self.num_aciertos += 1
            self.puntuacion += puntos

    def calcular_porcentaje(self):
        """
        Calcula el porcentaje de aciertos del usuario.
        """

        if self.num_ejercicios == 0:
            return 0

        return (self.num_aciertos / self.num_ejercicios) * 100

    def estadisticas(self):
        """
        Devuelve un resumen de las estadísticas del usuario.
        """

        return (
            f"Usuario: {self.nombre}\n"
            f"Puntuación: {self.puntuacion}\n"
            f"Ejercicios realizados: {self.num_ejercicios}\n"
            f"Aciertos: {self.num_aciertos}\n"
            f"Porcentaje de acierto: {self.calcular_porcentaje():.2f}%"
        )


    def __eq__(self, other):
        """
        Compara si dos usuarios son el mismo (mismo nombre).
        """

        if not isinstance(other, Usuario):
            return False

        return self.nombre == other.nombre

    def __lt__(self, other):
        """
        Permite comparar usuarios por puntuación.
        """

        if not isinstance(other, Usuario):
            return NotImplemented

        return self.puntuacion < other.puntuacion


    def __str__(self):
        return self.estadisticas()