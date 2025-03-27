from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

# Inicializamos la aplicación FastAPI.
app = FastAPI(title="Backend de Demostración")

# Configuramos el directorio donde se encuentran las plantillas HTML.
templates = Jinja2Templates(directory="templates")


@app.get("/landing", response_class=HTMLResponse)
async def landing(request: Request):
    """
    Endpoint que devuelve la página de Landing Page.
    """
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/policy_privacy", response_class=HTMLResponse)
async def politicas(request: Request):
    """
    Endpoint que devuelve la página de Políticas de Privacidad.
    """
    return templates.TemplateResponse("policy_privacy.html", {"request": request})

@app.get("/term_of_use", response_class=HTMLResponse)
async def terminos(request: Request):
    """
    Endpoint que devuelve la página de Términos de Uso.
    """
    return templates.TemplateResponse("term_of_use.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
