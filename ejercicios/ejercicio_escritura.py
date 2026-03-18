from ejercicios.ejercicio import Ejercicio

class EjercicioEscritura(Ejercicio):
    """
    Clase que representa un ejercicio de escritura.

    En este tipo de ejercicio el usuario debe escribir la traducción
    correcta de la palabra mostrada en la tarjeta.
    """

    def comprobar_respuesta(self, respuesta):
        """
        Comprueba si la respuesta del usuario es correcta.

        Parámetros:
        respuesta: str
            Respuesta escrita por el usuario.

        Devuelve:
        bool
            True si la respuesta es correcta, False en caso contrario.
        """
        self.respondido = True

        if self.tarjeta.es_correcta(respuesta):
            self.correcto = True
        else:
            self.correcto = False
        return self.correcto