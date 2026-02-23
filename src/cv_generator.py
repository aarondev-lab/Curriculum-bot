import os
from jinja2 import Environment, FileSystemLoader

def generar_cv(datos, plantilla="modern", output_path="cv.pdf"):
    """Genera un CV en PDF usando la plantilla especificada."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Mapeo de nombres de plantilla a archivos
    plantillas = {
        "modern": "modern.html",
        "classic": "classic.html",
        "creative": "creative.html"
    }
    
    if plantilla not in plantillas:
        raise ValueError(f"Plantilla no válida. Opciones: {list(plantillas.keys())}")
    
    template = env.get_template(plantillas[plantilla])
    html_content = template.render(datos)
    
    # Por ahora guardamos HTML, luego PDF con weasyprint
    html_output = output_path.replace('.pdf', '.html')
    with open(html_output, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ HTML generado: {html_output}")
    
    # Aquí iría la conversión a PDF con weasyprint (comentada por ahora)
    # from weasyprint import HTML
    # HTML(string=html_content).write_pdf(output_path)
    # print(f"✅ PDF generado: {output_path}")