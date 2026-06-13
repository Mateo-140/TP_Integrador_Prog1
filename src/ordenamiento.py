from src.datos import mostrar_paises

def solicitar_sentido():
    # Pregunta al usuario el sentido del ordenamiento (Ascendente o Descendente).
    
    opcion = input("A-Ascendente / D-Descendente: ").strip().upper()
    
    if opcion not in ("A", "D"):
        print("Opción inválida. Se usará Ascendente por defecto.")
        return False
    
    return opcion == "D"

def ordenar_nombre(paises):
    # Ordena y muestra los países alfabéticamente por nombre de manera Ascendente o Descendente.
    # Parámetros: paises (list)
    
    print("\n=== ORDENAR POR NOMBRE ===")
    rev = solicitar_sentido()
    ordenados = sorted(paises, key=lambda p: p["nombre"], reverse=rev)
    mostrar_paises(ordenados)

def ordenar_poblacion(paises):
    # Ordena y muestra los países por volumen de población de forma ascendente o descendente.
    # Parámetros: paises (list)
    
    print("\n=== ORDENAR POR POBLACIÓN ===")
    rev = solicitar_sentido()
    ordenados = sorted(paises, key=lambda p: p["poblacion"], reverse=rev)
    mostrar_paises(ordenados)

def ordenar_superficie(paises):
    # Ordena y muestra los países por su extensión territorial de forma ascendente o descendente.
    # Parámetros: paises (list)
    
    print("\n=== ORDENAR POR SUPERFICIE ===")
    rev = solicitar_sentido()
    ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=rev)
    mostrar_paises(ordenados)