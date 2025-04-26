from sqlalchemy.orm import Session
from model.ingrediente import Ingrediente
from typing import List
from sqlalchemy import or_


def get_ingredientes(db: Session):
    return db.query(Ingrediente).all()

def get_ingredientes_by_nomes(db: Session, nomes: List[str]):
    conditions = [Ingrediente.nome.ilike(nome) for nome in nomes]
    return db.query(Ingrediente).filter(or_(*conditions)).all()