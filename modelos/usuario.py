"""Módulo que define la clase Usuario."""


class Usuario:
    """
    Representa a un usuario y su progreso en los ejercicios.

    Atributos:
        nombre (str): Nombre del usuario.
        puntuacion (int): Puntuación total acumulada.
        num_ejercicios (int): Número de ejercicios realizados.
        num_aciertos (int): Número de ejercicios correctos.
    """

    def __init__(self, nombre: str, puntuacion: int = 0,
                 num_ejercicios: int = 0, num_aciertos: int = 0) -> None:
        """
        Inicializa el usuario.

        Parámetros:
            nombre (str): Nombre del usuario.
            puntuacion (int): Puntuación inicial.
            num_ejercicios (int): Ejercicios realizados inicialmente.
            num_aciertos (int): Aciertos iniciales.
        """
        self.nombre = nombre
        self.puntuacion = puntuacion
        self.num_ejercicios = num_ejercicios
        self.num_aciertos = num_aciertos

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del usuario."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """Establece el nombre validando que no esté vacío."""
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    def actualizar_progreso(self, correcto: bool, puntos: int | float) -> None:
        """
        Actualiza las estadísticas tras completar un ejercicio.

        Parámetros:
            correcto (bool): True si la respuesta fue correcta.
            puntos (int | float): Puntos obtenidos en el ejercicio.
        """
        self.num_ejercicios += 1
        if correcto:
            self.num_aciertos += 1
        self.puntuacion += puntos

    def calcular_porcentaje(self) -> float:
        """
        Calcula el porcentaje de aciertos sobre el total de ejercicios.

        Devuelve:
            float: Porcentaje de acierto (0.0 si no hay ejercicios).
        """
        if self.num_ejercicios == 0:
            return 0.0
        return (self.num_aciertos / self.num_ejercicios) * 100

    def estadisticas(self) -> str:
        """
        Devuelve un resumen de las estadísticas del usuario.

        Devuelve:
            str: Estadísticas formateadas.
        """
        return (
            f"Usuario: {self.nombre}\n"
            f"Puntuación: {self.puntuacion}\n"
            f"Ejercicios realizados: {self.num_ejercicios}\n"
            f"Aciertos: {self.num_aciertos}\n"
            f"Porcentaje de acierto: {self.calcular_porcentaje():.2f}%"
        )

    def __eq__(self, other: object) -> bool:
        """Compara dos usuarios por nombre."""
        if not isinstance(other, Usuario):
            return False
        return self.nombre == other.nombre

    def __str__(self) -> str:
        """Representación del usuario."""
        return self.estadisticas()