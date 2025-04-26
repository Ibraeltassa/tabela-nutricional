from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config.database import Base, db, SessionLocal
from service.ingrediente_service import get_ingredientes
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
    # Chama a função do serviço que consulta os ingredientes
    ingredientes = get_ingredientes(db)
    return ingredientes
