from config.database import SessionLocal
from model.ingrediente import Ingrediente
from scripts.dados import ingredientes


def popular_dados_iniciais():
    session = SessionLocal()
    try:
        if session.query(Ingrediente).first() is None:
            session.add_all(ingredientes)
            session.commit()
            print("Ingredientes criados.")
        else:
            print("Ingredientes já existem no banco.")
    except Exception as e:
        session.rollback()
        print(f"Erro ao popular dados: {e}")
    finally:
        session.close()
