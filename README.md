

## 📌 Descripción

Este proyecto fue realizado como parte de la actividad de introducción a **Prefect**, una herramienta de Python utilizada para crear y administrar flujos de trabajo.

Prefect permite organizar un programa en **tareas (Tasks)** y **flujos (Flows)**, facilitando la ejecución, seguimiento y control de los procesos.

---

## 🧰 Herramientas utilizadas

- 🐍 Python 3.12.1
- ⚙️ Prefect 3.8.7
- 🌐 Requests
- 📦 JSONPlaceholder
- 💻 Visual Studio Code

---

# 📝 Parte 1: Getting Started with Prefect

En la primera parte se siguió el tutorial de introducción a Prefect.

Se creó una tarea utilizando `@task` y un flujo utilizando `@flow`.

La tarea muestra un mensaje en pantalla:

```python
@task
def saludar():
    print("Hola desde una tarea de Prefect")
```

Después, esta tarea es ejecutada desde un flujo:

```python
@flow
def mi_flujo():
    saludar()
```

Al ejecutar el programa, Prefect registra la ejecución de la tarea y del flujo, mostrando que ambos terminaron correctamente.

---

# 🌐 Parte 2: Ejemplo con JSONPlaceholder

Para la segunda parte se modificó el ejemplo para trabajar con una API pública llamada **JSONPlaceholder**.

El programa obtiene información de dos recursos:

- Usuarios
- Publicaciones

Para realizar las peticiones HTTP se utilizó la librería `requests`.

El flujo está dividido en tres tareas:

### 1. Obtener usuarios

La primera tarea realiza una petición a la API y obtiene la información de los usuarios.

```python
@task
def obtener_usuarios():
```

### 2. Obtener publicaciones

La segunda tarea obtiene las publicaciones disponibles en la API.

```python
@task
def obtener_publicaciones():
```

### 3. Analizar los datos

La tercera tarea recibe los usuarios y publicaciones obtenidos anteriormente y genera un resumen.

```python
@task
def analizar_datos(usuarios, publicaciones):
```

El programa muestra cuántas publicaciones tiene cada usuario.

---

## 📊 Resultado obtenido

Al ejecutar el programa se obtuvieron:

- 👤 **10 usuarios**
- 📝 **100 publicaciones**
- 📊 **10 publicaciones por usuario**

Todos los usuarios obtenidos cuentan con 10 publicaciones en el conjunto de datos utilizado.

El flujo terminó correctamente y Prefect mostró las tareas como `Completed`.

---

## ⚙️ Funcionamiento

El flujo principal es:

```text
Inicio
  ↓
Obtener usuarios
  ↓
Obtener publicaciones
  ↓
Analizar datos
  ↓
Mostrar resumen
  ↓
Fin
```

Prefect se encarga de administrar la ejecución de las diferentes tareas que forman parte del flujo.

Durante la ejecución local, Prefect inicia temporalmente un servidor para administrar y registrar la ejecución del flujo.

---

## ▶️ Ejecución

Primero se activa el entorno virtual desde la terminal:

```bash
.venv\Scripts\activate
```

Después se ejecuta el programa:

```bash
python main.py
```

---

## 📁 Archivos del proyecto

```text
Perfect-phyton-clase9-11/
│
├── main.py
├── README.md
```

El entorno virtual `.venv` no se incluye en el repositorio, ya que contiene las dependencias instaladas localmente.

---
