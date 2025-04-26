from config.database import SessionLocal
from model.ingrediente import Ingrediente


def popular_dados_iniciais():
    session = SessionLocal()
    try:
        if session.query(Ingrediente).first() is None:
            ingredientes = [
                Ingrediente(nome="Arroz Branco", calorias=130.0,
                            proteinas=2.7, carboidratos=28.0, gorduras=0.3),
                Ingrediente(nome="Feijão Carioca", calorias=76.0,
                            proteinas=4.8, carboidratos=13.6, gorduras=0.5),
                Ingrediente(nome="Frango (peito grelhado)", calorias=165.0,
                            proteinas=31.0, carboidratos=0.0, gorduras=3.6),
                Ingrediente(nome="Brócolis", calorias=34.0,
                            proteinas=2.8, carboidratos=6.6, gorduras=0.4),
                Ingrediente(nome="Batata Doce", calorias=86.0,
                            proteinas=1.6, carboidratos=20.1, gorduras=0.1),
            ]

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
