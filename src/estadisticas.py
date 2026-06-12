
# ==========================================
# ESTADISTICAS
# ==========================================

def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadísticas generales del dataset de países.

    Indicadores mostrados:
        - País con mayor y menor población.
        - Promedio de población y superficie.
        - Cantidad de países por continente.

    Parámetros:
        paises (list): Lista de diccionarios con los datos de cada país.

    Retorna:
        None. Muestra los resultados por consola.
    """
    if not paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])

    promedio_poblacion = (
        sum(p["poblacion"] for p in paises) / len(paises)
    )

    promedio_superficie = (
        sum(p["superficie"] for p in paises) / len(paises)
    )

    # Conteo de países por continente
    continentes = {}

    for pais in paises:
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n========== ESTADÍSTICAS ==========")

    print(
        f"\nPaís con mayor población: "
        f"{mayor['nombre']} ({mayor['poblacion']:,} hab.)"
    )

    print(
        f"País con menor población: "
        f"{menor['nombre']} ({menor['poblacion']:,} hab.)"
    )

    print(f"\nPromedio de población:  {promedio_poblacion:>15,.2f} hab.")
    print(f"Promedio de superficie: {promedio_superficie:>15,.2f} km²")

    print("\nCantidad de países por continente:")
    print("-" * 35)

    for continente, cantidad in sorted(continentes.items()):
        print(f"  {continente:<25} {cantidad} país/es")

    print("=" * 35)
