import csv


# ==========================================
# CARGA DE DATOS
# ==========================================

def cargar_csv(nombre_archivo):
    """
    Carga los datos de países desde un archivo CSV.

    Parámetros:
        nombre_archivo (str): Ruta al archivo CSV.

    Retorna:
        list: Lista de diccionarios con los datos de cada país.
              Retorna lista vacía si el archivo no existe o está vacío.

    Excepciones controladas:
        FileNotFoundError: Si el archivo no existe.
        ValueError, KeyError: Si una fila tiene formato incorrecto.
    """
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "continente": fila["continente"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": float(fila["superficie"])
                    }

                    paises.append(pais)

                except (ValueError, KeyError):
                    print("Error en una fila del archivo CSV.")

    except FileNotFoundError:
        print("No se encontró el archivo.")

    return paises


# ==========================================
# GUARDAR CSV
# ==========================================

def guardar_csv(nombre_archivo, paises):
    """
    Guarda la lista de países en un archivo CSV.

    Parámetros:
        nombre_archivo (str): Ruta al archivo CSV de destino.
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None
    """
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "continente", "poblacion", "superficie"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)


# ==========================================
# MOSTRAR PAISES
# ==========================================

def mostrar_paises(lista):
    """
    Muestra por consola la lista de países con formato tabular.

    Parámetros:
        lista (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None
    """
    if not lista:
        print("\nNo hay resultados.")
        return

    print("\n" + "-" * 80)

    for pais in lista:

        print(
            f"{pais['nombre']:15}"
            f"{pais['continente']:20}"
            f"Población: {pais['poblacion']:12,}"
            f"  Superficie: {pais['superficie']:12,.0f}"
        )

    print("-" * 80)


# ==========================================
# BUSQUEDA
# ==========================================

def buscar_pais(paises):
    """
    Busca países por coincidencia parcial o exacta en el nombre.

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Muestra los resultados por consola.
    """
    texto = input("Ingrese nombre o parte del nombre: ").strip().lower()

    if not texto:
        print("Debe ingresar un texto para buscar.")
        return

    resultados = [p for p in paises if texto in p["nombre"].lower()]

    mostrar_paises(resultados)


# ==========================================
# FILTROS
# ==========================================

def filtrar_continente(paises):
    """
    Filtra y muestra países que pertenecen a un continente dado.

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Muestra los resultados por consola.
    """
    continente = input("Continente: ").strip().lower()

    if not continente:
        print("Debe ingresar un continente.")
        return

    resultados = [
        p for p in paises
        if p["continente"].lower() == continente
    ]

    mostrar_paises(resultados)


def filtrar_poblacion(paises):
    """
    Filtra y muestra países dentro de un rango de población.

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Muestra los resultados por consola.

    Excepciones controladas:
        ValueError: Si los valores ingresados no son numéricos.
    """
    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))

        if minimo > maximo:
            print("El mínimo no puede ser mayor al máximo.")
            return

    except ValueError:
        print("Error: ingrese valores numéricos enteros.")
        return

    resultados = [
        p for p in paises
        if minimo <= p["poblacion"] <= maximo
    ]

    mostrar_paises(resultados)


def filtrar_superficie(paises):
    """
    Filtra y muestra países dentro de un rango de superficie.

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Muestra los resultados por consola.

    Excepciones controladas:
        ValueError: Si los valores ingresados no son numéricos.
    """
    try:
        minimo = float(input("Superficie mínima (km²): "))
        maximo = float(input("Superficie máxima (km²): "))

        if minimo > maximo:
            print("El mínimo no puede ser mayor al máximo.")
            return

    except ValueError:
        print("Error: ingrese valores numéricos.")
        return

    resultados = [
        p for p in paises
        if minimo <= p["superficie"] <= maximo
    ]

    mostrar_paises(resultados)


# ==========================================
# ORDENAMIENTOS
# ==========================================

def ordenar_nombre(paises):
    """
    Ordena y muestra los países alfabéticamente por nombre (ascendente).

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Muestra los resultados por consola.
    """
    ordenados = sorted(paises, key=lambda p: p["nombre"])
    mostrar_paises(ordenados)


def ordenar_poblacion(paises):
    """
    Ordena y muestra los países por población de forma ascendente o descendente.

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Muestra los resultados por consola.
    """
    opcion = input("A-Ascendente / D-Descendente: ").strip().upper()

    if opcion not in ("A", "D"):
        print("Opción inválida. Ingrese A o D.")
        return

    reverse = opcion == "D"

    ordenados = sorted(paises, key=lambda p: p["poblacion"], reverse=reverse)

    mostrar_paises(ordenados)


def ordenar_superficie(paises):
    """
    Ordena y muestra los países por superficie de forma ascendente o descendente.

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Muestra los resultados por consola.
    """
    opcion = input("A-Ascendente / D-Descendente: ").strip().upper()

    if opcion not in ("A", "D"):
        print("Opción inválida. Ingrese A o D.")
        return

    reverse = opcion == "D"

    ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=reverse)

    mostrar_paises(ordenados)

