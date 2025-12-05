from sqlalchemy.orm import Session
from models import Jugador, Partido, EstadisticaJugador
from schemas import (
    JugadorCreate, PartidoCreate, EstadisticaCreate
)

def crear_jugador(db: Session, jugador_in: JugadorCreate) -> Jugador:
    jugador = Jugador(**jugador_in.model_dump())
    db.add(jugador)
    db.commit()
    db.refresh(jugador)
    return jugador


def listar_jugadores(db: Session):
    return db.query(Jugador).all()


def obtener_jugador(db: Session, jugador_id: int):
    return db.query(Jugador).filter(Jugador.id == jugador_id).first()


def actualizar_jugador(db: Session, jugador_id: int, jugador_in: JugadorCreate):
    jugador = obtener_jugador(db, jugador_id)
    if not jugador:
        return None
    for campo, valor in jugador_in.model_dump().items():
        setattr(jugador, campo, valor)
    db.commit()
    db.refresh(jugador)
    return jugador


def eliminar_jugador(db: Session, jugador_id: int):
    jugador = obtener_jugador(db, jugador_id)
    if not jugador:
        return False
    db.delete(jugador)
    db.commit()
    return True


def crear_partido(db: Session, partido_in: PartidoCreate) -> Partido:
    partido = Partido(**partido_in.model_dump())
    db.add(partido)
    db.commit()
    db.refresh(partido)
    return partido


def listar_partidos(db: Session):
    return db.query(Partido).all()


def obtener_partido(db: Session, partido_id: int):
    return db.query(Partido).filter(Partido.id == partido_id).first()


def actualizar_partido(db: Session, partido_id: int, partido_in: PartidoCreate):
    partido = obtener_partido(db, partido_id)
    if not partido:
        return None
    for campo, valor in partido_in.model_dump().items():
        setattr(partido, campo, valor)
    db.commit()
    db.refresh(partido)
    return partido
