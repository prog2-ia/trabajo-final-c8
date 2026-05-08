"""Módulo principal del sistema de práctica de vocabulario.

Gestiona la ejecución del programa mediante un menú interactivo que permite
realizar ejercicios, añadir tarjetas y consultar estadísticas.
"""

from modelos.tarjeta import Tarjeta
from modelos.mazo import Mazo
from modelos.usuario import Usuario
from datos.persistencia import Persistencia
from gestion.generador_ejercicios import GeneradorEjercicios


print("\n ***** SISTEMA DE PRÁCTICA DE VOCABULARIO ***** \n")

usuario, mazo = Persistencia.cargar()

if usuario is None or mazo is None:
    nombre = input("Introduce tu nombre: ")
    usuario = Usuario(nombre)

    t1 = Tarjeta("dog", "perro", "animales", 1)
    t2 = Tarjeta("cat", "gato", "animales", 1)
    t3 = Tarjeta("house", "casa", "objetos", 2)

    mazo = Mazo("Vocabulario básico")
    mazo.anadir_tarjeta(t1)
    mazo.anadir_tarjeta(t2)
    mazo.anadir_tarjeta(t3)
else:
    print(f"Datos cargados. Bienvenido de nuevo, {usuario.nombre}")


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

        generador = GeneradorEjercicios(mazo)
        ejercicios = generador.generar_escritura()

        for i, ejercicio in enumerate(ejercicios):

            ejercicio.mostrar()
            respuesta = input("Respuesta: ")

            try:
                correcto = ejercicio.comprobar_respuesta(respuesta)
                puntos = ejercicio.obtener_puntuacion()
                usuario.actualizar_progreso(correcto, puntos)

                print("Correcto" if correcto else "Incorrecto")

            except ValueError as e:
                print(f"Error: {e}")

            if i < len(ejercicios) - 1:
                if input("¿Quieres continuar? (s/n): ").lower() == "n":
                    break

    elif opcion == "2":

        generador = GeneradorEjercicios(mazo)
        ejercicios = generador.generar_test()

        for i, ejercicio in enumerate(ejercicios):

            ejercicio.mostrar()
            respuesta = input("Opción (A/B/C/D): ")

            try:
                correcto = ejercicio.comprobar_respuesta(respuesta)
                puntos = ejercicio.obtener_puntuacion()
                usuario.actualizar_progreso(correcto, puntos)

                print("Correcto" if correcto else "Incorrecto")

            except Exception as e:
                print(f"Error: {e}")

            if i < len(ejercicios) - 1:
                if input("¿Quieres continuar? (s/n): ").lower() == "n":
                    break

    elif opcion == "3":

        print("\n** AÑADIR TARJETA **")

        try:
            palabra = input("Palabra: ")
            traduccion = input("Traducción: ")
            categoria = input("Categoría: ")
            nivel = int(input("Nivel de dificultad (1-5): "))

            mazo.anadir_tarjeta(Tarjeta(palabra, traduccion, categoria, nivel))
            print(f"Tarjeta '{palabra}' añadida correctamente.")

        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == "4":

        print("\n*** ESTADÍSTICAS ***")
        print(usuario)

    elif opcion == "5":

        Persistencia.guardar(usuario, mazo)
        print("\nDatos guardados.")
        print("Fin del programa.")

    else:
        print("Opción no válida.")