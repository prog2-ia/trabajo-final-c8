from ejercicios.ejercicio import Ejercicio


class EjercicioEscritura(Ejercicio):
    """
    Ejercicio en el que el usuario escribe la traducción de una palabra.
    """

    def comprobar_respuesta(self, respuesta):
        """
        Comprueba si la respuesta es correcta.

        Parámetros:
            respuesta (str): Respuesta del usuario.

        Devuelve:
            bool: True si es correcta, False si no.
        """
        self.respondido = True

        if self.tarjeta.es_correcta(respuesta):
            self.correcto = True
        else:
            self.correcto = False

        return self.correcto