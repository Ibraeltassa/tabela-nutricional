from sqlalchemy.orm import Session
from model.ingrediente import Ingrediente
from typing import List
from sqlalchemy import or_


def get_ingredientes(db: Session):
    return db.query(Ingrediente).all()

def get_ingrediente_by_nome(db:Session, nome: str):
    return db.query(Ingrediente).filter(Ingrediente.nome.ilike(nome)).first()

def get_ingredientes_by_nomes(db: Session, nomes: List[str]):
    conditions = [Ingrediente.nome.ilike(nome) for nome in nomes]
    return db.query(Ingrediente).filter(or_(*conditions)).all()