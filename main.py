from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import Base, engine, get_db
import crud
import schemas


Base.metadata.create_all(bind=engine)

app = FastAPI(title="sigmotoa FC")


@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Bienvenido a sigmotoa FC {name}"}

templates = Jinja2Templates(directory="templates")


@app.post("/api/jugadores", response_model=schemas.Jugador)
def crear_jugador_api(jugador: schemas.JugadorCreate, db: Session = Depends(get_db)):
    return crud.crear_jugador(db, jugador)


@app.get("/api/jugadores", response_model=list[schemas.Jugador])
def listar_jugadores_api(db: Session = Depends(get_db)):
    return crud.listar_jugadores(db)


@app.get("/api/jugadores/{jugador_id}", response_model=schemas.Jugador)
def obtener_jugador_api(jugador_id: int, db: Session = Depends(get_db)):
    jugador = crud.obtener_jugador(db, jugador_id)
    return jugador

@app.post("/api/partidos", response_model=schemas.Partido)
def crear_partido_api(partido: schemas.PartidoCreate, db: Session = Depends(get_db)):
    return crud.crear_partido(db, partido)


@app.get("/api/partidos", response_model=list[schemas.Partido])
def listar_partidos_api(db: Session = Depends(get_db)):
    return crud.listar_partidos(db)
