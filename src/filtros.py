from src.datos import mostrar_paises

def filtrar_continente(paises):
    # Filtra y muestra los países pertenecientes a un continente específico,
    # ignorando de manera estricta mayúsculas, minúsculas y caracteres con tildes.
    # Parámetros: paises (list)
    
    print("\n=== FILTRAR POR CONTINENTE ===")
    busqueda = input("Ingrese el continente: ").strip().lower()

    if not busqueda:
        print("Error: el continente no puede estar vacío.")
        return

    def normalizar(texto):
        reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
        t = texto.lower()
        
        for tilde, reemp in reemplazos.items():
            t = t.replace(tilde, reemp)
        return t

    busqueda_limpia = normalizar(busqueda)
    resultados = [p for p in paises if normalizar(p["continente"]) == busqueda_limpia]

    if not resultados:
        print("No se encontraron países en el continente ingresado.")
    
    else:
        mostrar_paises(resultados)

def filtrar_poblacion(paises):
    # Filtra y muestra los países que se encuentren dentro de un rango de población.
    # Solicita los límites mínimo y máximo, y valida que sean números coherentes.
    # Parámetros: paises (list)
    
    print("\n=== FILTRAR POR RANGO DE POBLACIÓN ===")
    
    try:
        min_pob = int(input("Población mínima: "))
        max_pob = int(input("Población máxima: "))
        
        if min_pob < 0 or max_pob < 0 or min_pob > max_pob:
            print("Error: rangos numéricos inconsistentes.")
            return
    
    except ValueError:
        print("Error: Ingrese números enteros válidos.")
        return

    resultados = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]
    
    if not resultados:
        print("No se encontraron países en ese rango.")
    
    else:
        mostrar_paises(resultados)

def filtrar_superficie(paises):
    # Filtra y muestra los países que se encuentren dentro de un rango de superficie (km²).
    # Solicita los límites mínimo y máximo y realiza el control de errores numéricos.
    # Parámetros: paises (list)
    
    print("\n=== FILTRAR POR RANGO DE SUPERFICIE ===")
    
    try:
        min_sup = int(input("Superficie mínima (km²): "))
        max_sup = int(input("Superficie máxima (km²): "))
        
        if min_sup < 0 or max_sup < 0 or min_sup > max_sup:
            print("Error: rangos numéricos inconsistentes.")
            return
    
    except ValueError:
        print("Error: Ingrese números enteros válidos.")
        return

    resultados = [p for p in paises if min_sup <= p["superficie"] <= max_sup]
    
    if not resultados:
        print("No se encontraron países en ese rango.")
    
    else:
        mostrar_paises(resultados)