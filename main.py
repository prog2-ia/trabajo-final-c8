"""Modulo principal del sistema de práctica de vocabulario."""

import random
from modelos.tarjeta import Tarjeta
from modelos.mazo import Mazo
from modelos.usuario import Usuario
from ejercicios.ejercicio_escritura import EjercicioEscritura
from ejercicios.ejercicio_test import EjercicioTest
from datos.persistencia import Persistencia


print("\n=== SISTEMA DE PRÁCTICA DE VOCABULARIO ===\n")

# Cargar datos si existen
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

        Persistencia.guardar(usuario, mazo)
        print("\nDatos guardados.")
        print("Programa finalizado.")

    else:
        print("Opción no válida.")