"""Modulo principal del sistema de práctica de vocabulario.
Este módulo se encarga de gestionar la ejecución del programa mediante un menú interactivo
que permite al usuario practicar vocabulario, añadir nuevas tarjetas y consultar sus estadísticas.
Se inicializan los objetos principales del sistema como Usuario, Tarjeta y Mazo, y se utilizan
las clases de ejercicios para evaluar las respuestas del usuario. Además, controla el flujo
del programa mediante un bucle que gestiona las distintas opciones seleccionadas.
Funciones:
    - main (flujo principal implícito en el script)
    Controla la ejecución del programa mediante un menú interactivo.
Opciones del menú:
    - Ejercicio de escritura
    - Ejercicio tipo test
    - Añadir tarjeta al mazo
    - Ver estadísticas
    - Salir
Comportamiento:
    - Se solicita el nombre del usuario al iniciar el programa.
    - Se crea un mazo inicial con tarjetas de ejemplo.
    - Se ejecuta un bucle que muestra el menú hasta que el usuario decide salir.
    - Se actualiza el progreso del usuario tras cada ejercicio.
    - Se gestionan errores de entrada mediante excepciones.
"""

import random
from modelos.tarjeta import Tarjeta
from modelos.mazo import Mazo
from modelos.usuario import Usuario
from ejercicios.ejercicio_escritura import EjercicioEscritura
from ejercicios.ejercicio_test import EjercicioTest

print("\n=== SISTEMA DE PRÁCTICA DE VOCABULARIO ===\n")

nombre = input("Introduce tu nombre: ")
usuario = Usuario(nombre)

t1 = Tarjeta("dog", "perro", "animales", 1)
t2 = Tarjeta("cat", "gato", "animales", 1)
t3 = Tarjeta("house", "casa", "objetos", 2)

mazo = Mazo("Vocabulario básico")
mazo.anadir_tarjeta(t1)
mazo.anadir_tarjeta(t2)
mazo.anadir_tarjeta(t3)

opcion = ""

while opcion != "5":

    print("\n*** MENÚ ***")
    print("1. Ejercicio de escritura")
    print("2. Ejercicio tipo test")
    print("3. Añadir tarjeta al mazo")
    print("4. Ver estadísticas")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        tarjetas = mazo.tarjetas

        for i, tarjeta in enumerate(tarjetas):

            ejercicio = EjercicioEscritura(tarjeta)
            ejercicio.mostrar()

            respuesta = input("Respuesta: ")

            try:
                correcto = ejercicio.comprobar_respuesta(respuesta)
                puntos = ejercicio.obtener_puntuacion()

                usuario.actualizar_progreso(correcto, puntos)

                if correcto:
                    print("¡Correcto!")
                else:
                    print("Incorrecto. Respuesta correcta:", tarjeta.traduccion)

            except ValueError as e:
                print(f"Error: {e}")

            if i < len(tarjetas) - 1:
                continuar = input("¿Quieres continuar? (s/n): ")
                if continuar.lower() == "n":
                    break

    elif opcion == "2":

        tarjetas = mazo.tarjetas

        for i, tarjeta in enumerate(tarjetas):

            opciones = [t.traduccion for t in mazo.tarjetas if t != tarjeta]
            opciones = opciones[:3]
            opciones.append(tarjeta.traduccion)
            random.shuffle(opciones)

            ejercicio = EjercicioTest(tarjeta, opciones)
            ejercicio.mostrar()

            respuesta = input("Opción (A/B/C/D): ")

            try:
                correcto = ejercicio.comprobar_respuesta(respuesta)
                puntos = ejercicio.obtener_puntuacion()

                usuario.actualizar_progreso(correcto, puntos)

                if correcto:
                    print("¡Correcto!")
                else:
                    print("Incorrecto. Respuesta correcta:", tarjeta.traduccion)

            except (ValueError, IndexError) as e:
                print(f"Error: {e}")

            if i < len(tarjetas) - 1:
                continuar = input("¿Quieres continuar? (s/n): ")
                if continuar.lower() == "n":
                    break

    elif opcion == "3":

        print("\n** AÑADIR TARJETA **")

        try:
            palabra = input("Palabra: ")
            traduccion = input("Traducción: ")
            categoria = input("Categoría: ")
            nivel = int(input("Nivel de dificultad (1-5): "))

            nueva = Tarjeta(palabra, traduccion, categoria, nivel)
            mazo.anadir_tarjeta(nueva)

            print(f"Tarjeta '{palabra}' añadida correctamente.")

        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == "4":

        print("\n*** ESTADÍSTICAS ***")
        print(usuario)

    elif opcion == "5":

        print("\nPrograma finalizado.")

    else:
        print("Opción no válida.")