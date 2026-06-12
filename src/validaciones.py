
# ==========================================
# AGREGAR PAIS
# ==========================================

def agregar_pais(paises):
    """
    Solicita datos al usuario y agrega un nuevo país a la lista.

    Valida que ningún campo esté vacío, que los valores numéricos
    sean positivos y que el país no esté registrado previamente.

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Modifica la lista en memoria.

    Excepciones controladas:
        ValueError: Si población o superficie no son numéricos.
    """
    print("\n=== AGREGAR PAÍS ===")

    nombre = input("Nombre: ").strip()
    continente = input("Continente: ").strip()

    if not nombre or not continente:
        print("Error: no se permiten campos vacíos.")
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: ese país ya existe en el sistema.")
            return

    try:
        poblacion = int(input("Población: "))
        superficie = float(input("Superficie (km²): "))

        if poblacion <= 0 or superficie <= 0:
            print("Error: los valores deben ser positivos.")
            return

    except ValueError:
        print("Error: ingrese valores numéricos válidos.")
        return

    nuevo = {
        "nombre": nombre,
        "continente": continente,
        "poblacion": poblacion,
        "superficie": superficie
    }

    paises.append(nuevo)

    print(f"País '{nombre}' agregado correctamente.")


# ==========================================
# ACTUALIZAR PAIS
# ==========================================

def actualizar_pais(paises):
    """
    Actualiza la población y superficie de un país existente.

    Busca el país por nombre exacto (sin distinguir mayúsculas)
    y solicita los nuevos valores al usuario.

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Modifica el diccionario del país en memoria.

    Excepciones controladas:
        ValueError: Si los nuevos valores no son numéricos.
    """
    print("\n=== ACTUALIZAR PAÍS ===")

    nombre = input("Ingrese el nombre del país a actualizar: ").strip()

    if not nombre:
        print("Error: debe ingresar un nombre.")
        return

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            try:
                nueva_poblacion = int(input("Nueva población: "))
                nueva_superficie = float(input("Nueva superficie (km²): "))

                if nueva_poblacion <= 0 or nueva_superficie <= 0:
                    print("Error: los valores deben ser positivos.")
                    return

                pais["poblacion"] = nueva_poblacion
                pais["superficie"] = nueva_superficie

                print(f"Datos de '{pais['nombre']}' actualizados correctamente.")
                return

            except ValueError:
                print("Error: ingrese valores numéricos válidos.")
                return

    print(f"País '{nombre}' no encontrado.")
