from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import Response
from src.cv_generator import generate_cv_from_data

app = FastAPI()

@app.post("/generar-cv")
async def generar_cv(
    nombre: str = Form(...),
    email: str = Form(...),
    plantilla: str = Form("modern")
    # ... resto de campos (deberás añadirlos todos)
):
    # Construir el diccionario 'datos' con la misma estructura que espera tu plantilla
    datos = {
        "nombre": nombre,
        "email": email,
        # ... rellena con el resto de campos
        "educacion": [],  # Aquí tendrás que parsear los campos múltiples
        "experiencia": [],
        "habilidades": {"hard": [], "soft": []},
        "idiomas": []
    }

    try:
        pdf_bytes = generate_cv_from_data(datos, plantilla)
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=cv_{plantilla}.pdf"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "API Generador de CV funcionando"}