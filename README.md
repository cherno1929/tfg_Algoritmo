# 🧠 FTRLP Solver

Este repositorio contiene código en Python para ejecutar una aplicación web que resuelve el problema **FTRLP** (Fault-Tolerant Regenerator Location Problem) mediante un algoritmo especializado.

La aplicación incluye funciones para resolver el problema de forma básica, realizar benchmarks con distintos enfoques y crear grafos de forma manual para pruebas personalizadas.

## 🤖 Algoritmo

El algoritmo fue desarrollado para ubicar regeneradores en una red óptica, asegurando que las señales puedan llegar de un nodo a cualquier otro de la red, sin importar la distancia ni los posibles fallos. Esto mejora significativamente la **tolerancia a fallos** y la **fiabilidad de la comunicación** en redes ópticas.

## 🚀 Funcionalidades

- 🏗️ Generación y carga de grafos para su análisis.
- 📊 Ejecución de benchmarks con distintos algoritmos.
- ✏️ Creación manual de grafos y pruebas interactivas.

## 🛠️ Tecnologías

Este proyecto utiliza:

- **Backend**: Python / Flask / NetworkX  
- **Frontend**: HTML / CSS / JavaScript / D3JS

## ⚙️ ¿Cómo usarlo?

1. Clona o descarga este repositorio.
2. Instala las dependencias necesarias:
    ```bash
    pip install flask 
    ```
   
   ```bash
    pip install networkx 
    ```
   
   ```bash
    pip install matplotlib
    ```

3. Ejecuta la aplicación:
    ```bash
    python app.py
    ```
4. Abre tu navegador en `http://localhost:5000`.

---

