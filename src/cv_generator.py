import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# Ruta base: src/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Carpeta templates está al mismo nivel que src, así que subimos un nivel
TEMPLATES_DIR = os.path.join(BASE_DIR, '..', 'templates')

# Entorno Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def generate_cv_from_data(datos: dict, plantilla: str = "modern") -> bytes:
    """
    Genera un CV en PDF a partir de los datos y la plantilla elegida.
    
    Args:
        datos: Diccionario con la información personal, educación, experiencia, etc.
        plantilla: Nombre de la plantilla ('modern', 'classic', 'creative')
    
    Returns:
        bytes: Contenido del PDF generado en memoria.
    """
    # Mapeo de nombres de plantilla a archivos
    template_map = {
        "modern": "modern.html",
        "classic": "classic.html",
        "creative": "creative.html"
    }

    template_file = template_map.get(plantilla, "modern.html")

    try:
        template = env.get_template(template_file)
    except Exception as e:
        raise Exception(f"Error al cargar la plantilla {template_file}: {e}")

    # Renderizar HTML
    html_content = template.render(datos)

    # Generar PDF en memoria
    try:
        pdf_bytes = HTML(string=html_content).write_pdf()
        return pdf_bytes
    except Exception as e:
        raise Exception(f"Error al generar PDF: {e}")