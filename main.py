from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import Base, db, SessionLocal
from service.ingrediente_service import get_ingrediente_by_nome, get_ingredientes
from config.cache import get_cache, set_cache
from scripts.popular_dados import popular_dados_iniciais

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

# Endpoint que retorna todos os ingredientes
@app.get("/ingredientes")
def read_ingredientes(db: Session = Depends(get_db)):
    
    cache_key = "ingredientes_todos"
    ingredientes_cached = get_cache(cache_key)
    
    if ingredientes_cached:
        print("Passou pelo cache")
        return ingredientes_cached
    
    # Chama a função do serviço que consulta os ingredientes
    ingredientes = get_ingredientes(db)
    
    ingredientes_dict = [i.__dict__ for i in ingredientes]
    for i in ingredientes_dict:
        i.pop("_sa_instance_state", None)
    
    set_cache(cache_key, ingredientes_dict)
    
    return ingredientes_dict


@app.get("/ingredientes/{nome}")
def read_ingrediente(nome: str, db: Session = Depends(get_db)):
    ingrediente = get_ingrediente_by_nome(db, nome)
    if ingrediente is None:
        raise HTTPException(status_code=404, detail="Ingrediente não encontrado")
    return ingrediente