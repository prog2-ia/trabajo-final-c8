class Usuario:
    """
    Representa a un usuario y su progreso en los ejercicios.

    Atributos:
        nombre (str): Nombre del usuario.
        puntuacion (int): Puntuación total.
        num_ejercicios (int): Ejercicios realizados.
        num_aciertos (int): Ejercicios correctos.
    """

    def __init__(self, nombre, puntuacion=0, num_ejercicios=0, num_aciertos=0):
        """
        Inicializa el usuario.

        Parámetros:
            nombre (str): Nombre del usuario.
            puntuacion (int): Puntuación inicial.
            num_ejercicios (int): Ejercicios realizados.
            num_aciertos (int): Aciertos.
        """
        self.nombre = nombre
        self.puntuacion = puntuacion
        self.num_ejercicios = num_ejercicios
        self.num_aciertos = num_aciertos

    @property
    def nombre(self):
        """Devuelve el nombre."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre validando que no esté vacío."""
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    def actualizar_progreso(self, correcto, puntos):
        """
        Actualiza estadísticas tras un ejercicio.

        Parámetros:
            correcto (bool): Si la respuesta fue correcta.
            puntos (int): Puntos obtenidos.
        """
        self.num_ejercicios += 1
        if correcto:
            self.num_aciertos += 1
        self.puntuacion += puntos

    def calcular_porcentaje(self):
        """
        Calcula el porcentaje de aciertos.

        Devuelve:
            float: Porcentaje de acierto.
        """
        if self.num_ejercicios == 0:
            return 0
        return (self.num_aciertos / self.num_ejercicios) * 100

    def estadisticas(self):
        """
        Devuelve un resumen del usuario.

        Devuelve:
            str: Estadísticas del usuario.
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
        Compara dos usuarios por nombre.
        """
        if not isinstance(other, Usuario):
            return False
        return self.nombre == other.nombre

    def __str__(self):
        """Representación del usuario."""
        return self.estadisticas()