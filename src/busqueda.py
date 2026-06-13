from src.datos import mostrar_paises

def buscar_pais(paises):
    # Busca países cuyo nombre contenga el término ingresado por el usuario.
    # La búsqueda no discrimina entre mayúsculas y minúsculas (coincidencia parcial).
    # Parámetros: paises (list)
    
    print("\n=== BUSCAR PAÍS ===")
    busqueda = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()

    if not busqueda:
        print("Error: el término de búsqueda no puede estar vacío.")
        return

    resultados = [p for p in paises if busqueda in p["nombre"].lower()]

    if not resultados:
        print(f"No se encontraron países que coincidan con '{busqueda}'.")
    
    else:
        mostrar_paises(resultados)