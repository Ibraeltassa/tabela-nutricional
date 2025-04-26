from sqlalchemy.orm import Session
from model.ingrediente import Ingrediente


def get_ingredientes(db: Session):
    return db.query(Ingrediente).all()

def get_ingrediente_by_nome(db:Session, nome: str):
    return db.query(Ingrediente).filter(Ingrediente.nome.ilike(nome)).first()