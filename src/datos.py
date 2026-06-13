import csv

def cargar_csv(nombre_archivo):
    # Carga los datos de países desde un archivo CSV.
    # Parámetros: nombre_archivo (str)
    # Retorna: list de diccionarios

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
                        "superficie": int(fila["superficie"])
                    }

                    paises.append(pais)
                except (ValueError, KeyError):
                    print("Error en una fila del archivo CSV.")
    
    except FileNotFoundError:
        print("No se encontró el archivo base de datos.")
    
    return paises

def guardar_csv(nombre_archivo, paises):
    # Guarda la lista de países en el archivo CSV especificado de forma persistente.
    # Parámetros: nombre_archivo (str), paises (list)
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "continente", "poblacion", "superficie"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            
            for pais in paises:
                escritor.writerow(pais)
    
    except Exception:
        print("Error al intentar guardar los datos en el archivo.")

def mostrar_paises(paises):
    # Muestra la lista de países completa formateada en forma de tabla por consola.
    # Parámetros: paises (list)
    
    if not paises:
        print("No hay países para mostrar.")
        return
    
    print(f"\n{'NOMBRE':<25} {'CONTINENTE':<20} {'POBLACIÓN':<15} {'SUPERFICIE (km²)':<15}")
    print("-" * 75)
    
    for p in paises:
        print(f"{p['nombre']:<25} {p['continente']:<20} {p['poblacion']:<15,} {p['superficie']:<15,}")