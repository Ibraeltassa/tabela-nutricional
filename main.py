from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import Base, db, SessionLocal
from model.ingrediente import Ingrediente
from service.ingrediente_service import get_ingredientes, get_ingredientes_by_nomes
from config.cache import get_cache, set_cache
from scripts.popular_dados import popular_dados_iniciais
from dto.ingrediente_request import IngredientesRequestDTO

app = FastAPI(
    title="API de Tabela Nutricional",
    description="Fornece informações nutricionais de ingredientes para integração com a API de receitas",
    version="1.1.0"
)

Base.metadata.create_all(bind=db)

popular_dados_iniciais()

def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


@app.get("/ingredientes")
def read_ingredientes(db: Session = Depends(get_db)):
    
    cache_key = "ingredientes_todos"
    ingredientes_cached = get_cache(cache_key)
    
    if ingredientes_cached:
        return ingredientes_cached

    ingredientes = get_ingredientes(db)
    
    ingredientes_dict = [i.__dict__ for i in ingredientes]
    for i in ingredientes_dict:
        i.pop("_sa_instance_state", None)
    
    set_cache(cache_key, ingredientes_dict)
    
    return ingredientes_dict

@app.post("/ingredientes/buscar-por-lista")
def buscar_ingredientes_por_lista(request: IngredientesRequestDTO, db: Session = Depends(get_db)):

    nomes_ordenados = sorted(request.nomes)
    cache_key = "ingredientes_" + "_".join(nomes_ordenados)
    ingredientes_cached = get_cache(cache_key)

    if ingredientes_cached:
        print("Passou pelo cache")
        return ingredientes_cached
    
    ingredientes = get_ingredientes_by_nomes(db, request.nomes)
    
    ingredientes_dict = [i.__dict__ for i in ingredientes]

    for ingrediente in ingredientes_dict:
        ingrediente.pop("_sa_instance_state", None)

    set_cache(cache_key, ingredientes_dict)
    return ingredientes_dict