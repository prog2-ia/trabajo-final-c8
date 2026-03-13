class Usuario:
    """
    Clase que representa a un usuario del sistema.

    Almacena información sobre el progreso del usuario en los ejercicios
    de vocabulario, incluyendo su puntuación total, número de ejercicios
    realizados y número de aciertos.

    Permite actualizar estadísticas tras cada ejercicio, calcular el
    porcentaje de aciertos y comparar usuarios según su rendimiento.

    Atributos:
    nombre : str
        Nombre del usuario.
    puntuacion : int
        Puntuación total acumulada por el usuario.
    num_ejercicios : int
        Número total de ejercicios realizados.
    num_aciertos : int
        Número de ejercicios respondidos correctamente.

    Métodos:
    __init__(self, nombre, puntuacion=0, num_ejercicios=0, num_aciertos=0)
        Inicializa un nuevo usuario con sus estadísticas.

    actualizar_progreso(correcto : bool, puntos : int) -> None
        Actualiza las estadísticas del usuario tras realizar un ejercicio.

    calcular_porcentaje() -> float
        Calcula el porcentaje de aciertos del usuario.

    estadisticas() -> str
        Devuelve un resumen de las estadísticas del usuario.

    __eq__(other) -> bool
        Permite comparar si dos usuarios son iguales según su nombre.

    __lt__(other) -> bool
        Permite comparar usuarios según su puntuación.

    __str__() -> str
        Devuelve una representación en texto de las estadísticas del usuario.
    """

    def __init__(self, nombre, puntuacion=0, num_ejercicios=0, num_aciertos=0):
        """
        Inicializa una instancia de la clase Usuario.

        Parámetros:
        nombre : str
            Nombre del usuario.
        puntuacion : int
            Puntuación inicial del usuario.
        num_ejercicios : int
            Número inicial de ejercicios realizados.
        num_aciertos : int
            Número inicial de aciertos.
        """
        self.nombre = nombre
        self.puntuacion = puntuacion
        self.num_ejercicios = num_ejercicios
        self.num_aciertos = num_aciertos

    @property
    def nombre(self):
        """Devuelve el nombre del usuario."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Establece el nombre del usuario validando que no esté vacío."""
        if not valor or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    def actualizar_progreso(self, correcto, puntos):
        """
        Actualiza las estadísticas del usuario tras completar un ejercicio.

        Parámetros:
        correcto : bool
            Indica si el ejercicio fue respondido correctamente.
        puntos : int
            Puntos obtenidos en el ejercicio.
        """

        self.num_ejercicios += 1

        if correcto:
            self.num_aciertos += 1
            self.puntuacion += puntos

    def calcular_porcentaje(self):
        """
        Calcula el porcentaje de aciertos del usuario.

        Devuelve:
        float
            Porcentaje de aciertos sobre el total de ejercicios realizados.
        """

        if self.num_ejercicios == 0:
            return 0

        return (self.num_aciertos / self.num_ejercicios) * 100

    def estadisticas(self):
        """
        Devuelve un resumen de las estadísticas del usuario.

        Devuelve:
        str
            Información del usuario y su rendimiento.
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
        Compara si dos usuarios son iguales según su nombre.
        """

        if not isinstance(other, Usuario):
            return False

        return self.nombre == other.nombre

    def __eq__(self, other):
        """
        Permite comprobar si dos usuarios son iguales.
        Se consideran iguales si tienen el mismo nombre.
        """
        if not isinstance(other, Usuario):
            return False

        return self.nombre == other.nombre

    def __str__(self):
        """
        Devuelve una representación en texto del usuario.
        """

        return self.estadisticas()