# ==========================================
# AGREGAR PAIS
# ==========================================

def agregar_pais(paises):
    # Solicita datos al usuario y agrega un nuevo país a la lista.
    # Valida campos vacíos, nombres numéricos, valores positivos y
    # permite ingresar continentes sin importar mayúsculas o tildes.
    
    print("\n=== AGREGAR PAÍS ===")
    nombre_raw = input("Nombre: ").strip()
    continente_raw = input("Continente: ").strip()

    if not nombre_raw or not continente_raw:
        print("Error: no se permiten campos vacíos.")
        return

    if nombre_raw.isdigit():
        print("Error: El nombre del país no puede estar compuesto únicamente por números.")
        return

    nombre = nombre_raw.title()

    # Lista oficial con el formato estético para la base de datos
    
    continentes_validos = ["América Del Sur", "América Del Norte", "Europa", "Asia", "África", "Oceanía"]

    # Función interna para quitar tildes y pasar a minúsculas
    
    def normalizar(texto):
        reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
        t = texto.lower()
        for tilde, reemp in reemplazos.items():
            t = t.replace(tilde, reemp)
        return t

    # Normalizamos la entrada del usuario (ej: "america del sur")
    
    continente_usuario_limpio = normalizar(continente_raw)

    # Creamos una lista de los válidos pero también normalizados
    
    continentes_validos_limpios = [normalizar(c) for c in continentes_validos]

    # Comparamos limpiamente sin que afecten las tildes ni las mayúsculas
    
    if continente_usuario_limpio not in continentes_validos_limpios:
        print(f"Error: Continente inválido. Permitidos: {', '.join(continentes_validos)}")
        return
    
    # Si es válido, obtenemos el formato lindo ("América Del Sur") para guardarlo bien en el CSV
    
    indice = continentes_validos_limpios.index(continente_usuario_limpio)
    continente_correcto = continentes_validos[indice]

    for pais in paises:
    
        if pais["nombre"].lower() == nombre.lower():
            print("Error: ese país ya existe en el sistema.")
            return

    try:
        poblacion_input = input("Población: ").strip().replace(".", "")
        superficie_input = input("Superficie (km²): ").strip().replace(".", "")

        poblacion = int(poblacion_input)
        superficie = int(superficie_input)

        if poblacion <= 0 or superficie <= 0:
            print("Error: los valores deben ser mayores a cero.")
            return
    
    except ValueError:
        print("Error: Debe ingresar un número entero válido para población y superficie.")
        return

    # Guardamos el país con el continente perfectamente estandarizado
    
    paises.append({"nombre": nombre, "continente": continente_correcto, "poblacion": poblacion, "superficie": superficie})
    print(f"País '{nombre}' agregado exitosamente.")

# ==========================================
# ACTUALIZAR PAIS
# ==========================================

def actualizar_pais(paises):
    # Actualiza la población y superficie de un país existente.
    # Busca el país por nombre exacto (sin distinguir mayúsculas) y solicita los
    # nuevos valores al usuario, permitiendo puntos como separadores de miles
    # y guardando la superficie de manera estricta como entero (int).
    # Parámetros: paises (list)
    
    print("\n=== ACTUALIZAR PAÍS ===")
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()

    if not nombre:
        print("Error: debe ingresar un nombre.")
        return

    for pais in paises:
        
        if pais["nombre"].lower() == nombre.lower():
        
            try:
                # NUEVA MEJORA: Se leen las entradas limpiando los puntos antes de convertir
                
                poblacion_input = input("Nueva población: ").strip().replace(".", "")
                superficie_input = input("Nueva superficie (km²): ").strip().replace(".", "")

                nueva_poblacion = int(poblacion_input)
                nueva_superficie = int(superficie_input)

                if nueva_poblacion <= 0 or nueva_superficie <= 0:
                    print("Error: los valores deben ser mayores a cero.")
                    return

                pais["poblacion"] = nueva_poblacion
                pais["superficie"] = nueva_superficie
                print(f"Datos de '{pais['nombre']}' actualizados correctamente.")
                return
            
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
                return
    
    print(f"País '{nombre}' no encontrado.")