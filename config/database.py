from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("postgresql://user:password@localhost:5434/tabela-nutricional", echo=True)

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

