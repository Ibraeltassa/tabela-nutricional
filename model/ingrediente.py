from config.database import Base
from sqlalchemy import Column, Integer, String, Float


class Ingrediente(Base):
    __tablename__ = "tb_ingredientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    calorias = Column(Float)
    proteinas = Column(Float)
    carboidratos = Column(Float)
    gorduras = Column(Float)
    quantidade_base = Column(String)

    def __init__(self, nome, calorias, proteinas, carboidratos, gorduras, quantidade_base="100g"):
        self.nome = nome
        self.calorias = calorias
        self.proteinas = proteinas
        self.carboidratos = carboidratos
        self.gorduras = gorduras
        self.quantidade_base = quantidade_base
