from typing import List, Optional
from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel

from importilo_meetup import importas_el_meetup


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
