# Gestión de Datos de Países en Python

Este proyecto es el **Trabajo Práctico Integrador (TPI)** para la materia **Programación 1** de la *Tecnicatura Universitaria en Programación a Distancia (UTN)*. Consiste en una aplicación de consola desarrollada en Python 3.x que permite administrar, filtrar, ordenar y calcular estadísticas sobre un dataset de países almacenado en formato CSV.

---

## 👥 Integrantes
Braian Martínez: desarrollo principal y edición de código, revisión.
Mateo Peralta: documentación tecnica, correcciones y optimización del sistema.

---

## 📝 Descripción del Proyecto
Este sistema es una aplicación de consola desarrollada en **Python 3.x** diseñada para la administración, filtrado y análisis estadístico de un dataset de países. El software fue migrado exitosamente de un script único hacia una **arquitectura modular de 7 componentes**, aplicando los principios de responsabilidad única y persistencia de datos mediante archivos **CSV**.

### 🛡️ Ingeniería de Robustez e Integridad (QA)
El sistema cuenta con un blindaje contra errores lógicos habituales de carga:
* **Sanitización de Puntos:** Permite ingresar números con puntos de miles (ej: `46.285.124` o `2.700.000`) en altas, actualizaciones y filtros numéricos, limpiándolos elásticamente para evitar caídas del sistema (`ValueError`).
* **Flexibilidad de Caracteres:** El motor de búsqueda y alta de continentes normaliza las entradas. Podés escribir `america del sur`, `ÁFRICA` o `Europa` con o sin tildes/mayúsculas, y el sistema lo procesará de manera correcta y estética.
* **Validaciones de Entrada:** Restringe nombres puramente numéricos y asegura que la población y superficie sean variables estrictamente mayores a cero ($>0$).

---

## 📦 Estructura Modular del Código (`src/`)
La lógica del negocio se encuentra distribuida estratégicamente en los siguientes archivos:
* `main.py`: Orquestador central del menú de opciones y ciclo de vida de la app.
* `datos.py`: Gestión de operaciones de lectura/escritura (I/O) en `paises.csv` y renderizado de tablas.
* `validaciones.py`: Controladores de mutación segura de datos (Altas y Actualizaciones).
* `busquedas.py`: Algoritmos de exploración y coincidencia parcial por nombre.
* `filtros.py`: Rutinas de extracción sectorizada por continente y rangos cuantitativos.
* `ordenamiento.py`: Clasificación posicional (Ascendente / Descendente) mediante claves lambda.
* `estadisticas.py`: Análisis matemático y cálculo de métricas agregadas del dataset.

---

## 🚀 Instrucciones de Instalación y Ejecución

### Requisitos Previos
* Tener instalado **Python 3.10** o superior.
* Disponer del archivo de datos `paises.csv` dentro de la carpeta raíz o la carpeta `src/`.

### Ejecución del Sistema
Para garantizar que Python reconozca el paquete modular de manera interna sin conflictos de importación circular, la aplicación debe ejecutarse desde la **carpeta raíz del proyecto** abriendo una terminal y corriendo el siguiente comando:

```bash
python -m src.main
```
---
💡Ejemplos Prácticos de Uso
1. Agregar un País (Tolerante a minúsculas/tildes)
Entrada en Consola:

Plaintext
Nombre: Peru
Continente: america del sur
Población: 34.000.000
Superficie (km²): 1.285.216
Resultado: El sistema valida los datos de forma limpia, remueve los puntos internamente y registra de forma estética en el CSV: Peru,América Del Sur,34000000,1285216.

---
📎Link.
You tube: https://youtu.be/qe8kJ0Rlx-E
