# 📄 API Generadora de CV Automáticos

Esta API, construida con **FastAPI**, permite generar currículums vitae (CV) en formato PDF a partir de datos personales proporcionados por el usuario. Utiliza plantillas HTML (Jinja2) y convierte el resultado a PDF gracias a **WeasyPrint**.

El proyecto está pensado para ser consumido desde un frontend (por ejemplo, tu portfolio en Astro) o para pruebas locales mediante herramientas como `curl` o la documentación interactiva de FastAPI.

---

## 🚀 Características

- Generación de CV en PDF con **tres plantillas diferentes** (moderna, clásica, creativa).
- Datos de entrada flexibles (nombre, email, educación, experiencia, habilidades, idiomas, etc.).
- API REST documentada automáticamente con Swagger UI.
- Fácil integración con cualquier frontend mediante peticiones HTTP.
- Separación clara entre lógica de negocio (Python) y presentación (HTML/CSS).

---

## 🛠️ Tecnologías utilizadas

- **Python 3.8+**
- **FastAPI** – Framework para la API.
- **Jinja2** – Motor de plantillas para generar el HTML del CV.
- **WeasyPrint** – Conversión de HTML a PDF.
- **Uvicorn** – Servidor ASGI para ejecutar la API.
- **pdfkit** - Genera repores pdf

---

## 📁 Estructura del proyecto

<!-- cv-generator/
├── src/
│ ├── init.py # Convierte src en un paquete Python
│ ├── api.py # Endpoints de la API (FastAPI)
│ ├── cv_generator.py # Lógica de generación de CV (Jinja2 + WeasyPrint)
│ └── (otros archivos opcionales)
├── templates/ # Plantillas HTML para los CV
│ ├── modern.html
│ ├── classic.html
│ └── creative.html
├── venv/ # Entorno virtual (ignorado por Git)
├── requirements.txt # Dependencias
└── README.md # Este archivo !-->

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/aarondev-lab/cv-generator.git
cd cv-generator
```
### 2. Creacion entorno virtual (recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

```
### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```
### 4. Ejecutar la api

```bash
uvicorn src.api:app --reload --> url "http://127.0.0.1:8000/docs"

```
