from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine(
    "postgresql://user:password@tb-nutricional-database:5432/tabela-nutricional", echo=True)

SessionLocal = sessionmaker(bind=db)


Base = declarative_base()
