import os
import sys
sys.path.insert(0, os.path.dirname(__file__))  # para importar módulos locales
from data_collector import obtener_datos
from cv_generator import generar_cv

def main():
    print("Generador automático de CV")
    print("=" * 35)

    # Obtener datos (aquí podrías cargar de JSON o preguntar)
    # Por ahora usamos datos de ejemplo
    datos = {
        "nombre": "Aarón García Sánchez",
        "email": "aaron.garcia@email.com",
        "telefono": "+34 123 456 789",
        "direccion": "Málaga, España",
        "perfil": "Estudiante de máster en Ciberseguridad con experiencia en desarrollo web y análisis de logs. Apasionado por la tecnología y el deporte.",
        "educacion": [
            {"titulo": "Máster en Ciberseguridad", "institucion": "Universidad de Málaga", "fecha": "2024-2026", "descripcion": "Especialización en forense digital y pentesting."},
            {"titulo": "Grado en Ingeniería Informática", "institucion": "Universidad de Málaga", "fecha": "2020-2024", "descripcion": "Especialidad en Ingeniería de Computadores."}
        ],
        "experiencia": [
            {"puesto": "Desarrollador Backend (Prácticas)", "empresa": "Tech Solutions", "fecha": "2023-2024", "descripcion": "Desarrollo de aplicaciones web con Symfony y MySQL."},
            {"puesto": "Asistente Técnico", "empresa": "InfoSys", "fecha": "2022-2023", "descripcion": "Soporte técnico y mantenimiento de sistemas."}
        ],
        "habilidades": {
            "hard": ["Python", "JavaScript", "Symfony", "MongoDB", "Tailwind", "Astro"],
            "soft": ["Trabajo en equipo", "Comunicación", "Resolución de problemas", "Adaptabilidad"]
        },
        "idiomas": [
            {"idioma": "Español", "nivel": "Nativo"},
            {"idioma": "Inglés", "nivel": "B2 (en curso C1)"}
        ],
        "certificaciones": [
            {"nombre": "Certificación en Ciberseguridad", "entidad": "Cisco", "fecha": "2023"},
            {"nombre": "Curso de Python Avanzado", "entidad": "Udemy", "fecha": "2022"}
        ],
        "proyectos": [
            {"nombre": "Analizador de logs", "descripcion": "Script en Python para detectar ataques de fuerza bruta y escaneo de puertos."},
            {"nombre": "Banco Digital", "descripcion": "Aplicación web con Symfony y MySQL."}
        ]
    }

    print("Datos cargados para:", datos["nombre"])

    # Preguntar qué plantilla usar
    print("\nPlantillas disponibles:")
    print("1. Moderna")
    print("2. Clásica")
    print("3. Creativa")
    opcion = input("Elige una opción (1/2/3): ").strip()

    mapa = {"1": "modern", "2": "classic", "3": "creative"}
    plantilla = mapa.get(opcion, "modern")

    # Crear carpeta 'output' si no existe
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Definir la ruta de salida dentro de output
    output_filename = f"cv_{plantilla}.pdf"
    output_path = os.path.join(output_dir, output_filename)

    print(f"\nGenerando CV con plantilla {plantilla}...")
    generar_cv(datos, plantilla=plantilla, output_path=output_path)
    print(f"✅ CV guardado en: {output_path}")

if __name__ == "__main__":
    main()