from typing import List, Optional
from enum import Enum

from fastapi import FastAPI, status, applications
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel

from importilaj_funkcioj import importas_el_meetup


# Fiksu swagger_ui versio
def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args,
        **kwargs,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.30.0/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.30.0/swagger-ui.css"
    )


applications.get_swagger_ui_html = swagger_monkey_patch


class ImportPeto(BaseModel):
    URL: str


class Evento(BaseModel):
    titolo: str
    urbo: Optional[str]
    ligilo: str
    reta: bool
    landa_id: str
    latitudo: Optional[str]
    longitudo: Optional[str]
    adreso: str
    horzono: str
    komenco: str
    fino: str
    enhavo: str
    priskribo: str


class Fonto(BaseModel):
    nomo: str
    priskribo: Optional[str] = None


fontoj = [{"nomo": "Meetup"}, {"nomo": "Duolingo"}]


class FontNomoj(str, Enum):
    meetup = "meetup"
    duolingo = "duolingo"


app = FastAPI()


@app.get("/")
async def root():
    return {"mesaĝo": "Saluton SEPanoj!"}


@app.get("/fontoj", status_code=status.HTTP_200_OK, response_model=List[Fonto])
async def legu_fontojn():
    return fontoj


@app.post("/meetup", status_code=status.HTTP_200_OK, response_model=Evento)
async def importu_el_meetup(importPeto: ImportPeto):
    return importas_el_meetup(importPeto.URL)
