from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import Response
from src.cv_generator import generate_cv_from_data

app = FastAPI(title="Generador de CV API")

@app.post("/generar-cv")
async def generar_cv(
    # Datos personales
    nombre: str = Form(...),
    email: str = Form(...),
    telefono: str = Form(""),
    direccion: str = Form(""),
    perfil: str = Form(""),

    # Educación (campos múltiples separados por |)
    educacion_titulos: str = Form(""),
    educacion_instituciones: str = Form(""),
    educacion_fechas: str = Form(""),
    educacion_descripciones: str = Form(""),

    # Experiencia (campos múltiples separados por |)
    experiencia_puestos: str = Form(""),
    experiencia_empresas: str = Form(""),
    experiencia_fechas: str = Form(""),
    experiencia_descripciones: str = Form(""),

    # Habilidades
    habilidades_hard: str = Form(""),
    habilidades_soft: str = Form(""),

    # Idiomas
    idiomas_nombres: str = Form(""),
    idiomas_niveles: str = Form(""),

    # Certificaciones (opcional)
    certificaciones_nombres: str = Form(""),
    certificaciones_entidades: str = Form(""),
    certificaciones_fechas: str = Form(""),

    # Proyectos (opcional)
    proyectos_nombres: str = Form(""),
    proyectos_descripciones: str = Form(""),

    # Plantilla
    plantilla: str = Form("modern")
):
    try:
        # Construir el diccionario de datos en el formato que espera la plantilla
        datos = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono,
            "direccion": direccion,
            "perfil": perfil,
            "educacion": [
                {
                    "titulo": t.strip(),
                    "institucion": i.strip(),
                    "fecha": f.strip(),
                    "descripcion": d.strip() if d else ""
                }
                for t, i, f, d in zip(
                    educacion_titulos.split("|") if educacion_titulos else [],
                    educacion_instituciones.split("|") if educacion_instituciones else [],
                    educacion_fechas.split("|") if educacion_fechas else [],
                    educacion_descripciones.split("|") if educacion_descripciones else []
                )
            ],
            "experiencia": [
                {
                    "puesto": p.strip(),
                    "empresa": e.strip(),
                    "fecha": f.strip(),
                    "descripcion": d.strip() if d else ""
                }
                for p, e, f, d in zip(
                    experiencia_puestos.split("|") if experiencia_puestos else [],
                    experiencia_empresas.split("|") if experiencia_empresas else [],
                    experiencia_fechas.split("|") if experiencia_fechas else [],
                    experiencia_descripciones.split("|") if experiencia_descripciones else []
                )
            ],
            "habilidades": {
                "hard": [h.strip() for h in habilidades_hard.split("|") if h.strip()],
                "soft": [s.strip() for s in habilidades_soft.split("|") if s.strip()]
            },
            "idiomas": [
                {"idioma": nom.strip(), "nivel": niv.strip()}
                for nom, niv in zip(
                    idiomas_nombres.split("|") if idiomas_nombres else [],
                    idiomas_niveles.split("|") if idiomas_niveles else []
                )
            ],
            "certificaciones": [
                {
                    "nombre": nom.strip(),
                    "entidad": ent.strip(),
                    "fecha": fec.strip()
                }
                for nom, ent, fec in zip(
                    certificaciones_nombres.split("|") if certificaciones_nombres else [],
                    certificaciones_entidades.split("|") if certificaciones_entidades else [],
                    certificaciones_fechas.split("|") if certificaciones_fechas else []
                )
            ],
            "proyectos": [
                {"nombre": nom.strip(), "descripcion": desc.strip()}
                for nom, desc in zip(
                    proyectos_nombres.split("|") if proyectos_nombres else [],
                    proyectos_descripciones.split("|") if proyectos_descripciones else []
                )
            ]
        }

        # Generar PDF
        pdf_bytes = generate_cv_from_data(datos, plantilla)

        # Devolver el PDF como respuesta
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=cv_{plantilla}.pdf"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "API Generador de CV funcionando"}