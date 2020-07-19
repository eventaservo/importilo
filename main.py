from typing import List, Optional
from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel


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
