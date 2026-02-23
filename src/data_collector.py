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
def obtener_datos():
    # Aquí podrías implementar la entrada interactiva o carga de JSON
    # Por ahora retorna None para que main use datos de ejemplo
    return None