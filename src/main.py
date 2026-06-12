import os
from src.funciones import (
    cargar_csv,
    guardar_csv,
    mostrar_paises,
    buscar_pais,
    filtrar_continente,
    filtrar_poblacion,
    filtrar_superficie,
    ordenar_nombre,
    ordenar_poblacion,
    ordenar_superficie
)
from src.validaciones import agregar_pais, actualizar_pais
from src.estadisticas import mostrar_estadisticas


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu():
    """
    Muestra el menú principal del sistema y gestiona la navegación.

    Carga el archivo CSV al inicio, ejecuta la opción seleccionada
    por el usuario y guarda los cambios cuando corresponde.

    Retorna:
        None
    """
    ARCHIVO = os.path.join("data", "paises.csv")

    paises = cargar_csv(ARCHIVO)

    while True:

        print("\n========== MENÚ PRINCIPAL ==========")
        print("1.  Agregar país")
        print("2.  Actualizar país")
        print("3.  Buscar país")
        print("4.  Filtrar por continente")
        print("5.  Filtrar por población")
        print("6.  Filtrar por superficie")
        print("7.  Ordenar por nombre")
        print("8.  Ordenar por población")
        print("9.  Ordenar por superficie")
        print("10. Mostrar estadísticas")
        print("11. Mostrar todos los países")
        print("0.  Salir")
        print("=====================================")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
            guardar_csv(ARCHIVO, paises)

        elif opcion == "2":
            actualizar_pais(paises)
            guardar_csv(ARCHIVO, paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_continente(paises)

        elif opcion == "5":
            filtrar_poblacion(paises)

        elif opcion == "6":
            filtrar_superficie(paises)

        elif opcion == "7":
            ordenar_nombre(paises)

        elif opcion == "8":
            ordenar_poblacion(paises)

        elif opcion == "9":
            ordenar_superficie(paises)

        elif opcion == "10":
            mostrar_estadisticas(paises)

        elif opcion == "11":
            mostrar_paises(paises)

        elif opcion == "0":
            print("Programa finalizado. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Ingrese un número del 0 al 11.")


# ==========================================
# INICIO DEL PROGRAMA
# ==========================================

if __name__ == "__main__":
    menu()
