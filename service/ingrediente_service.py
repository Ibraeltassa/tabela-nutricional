from sqlalchemy.orm import Session
from model.ingrediente import Ingrediente


def get_ingredientes(db: Session):
    return db.query(Ingrediente).all()
