from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()

class Animes(Base):
    __tablename__ = "animes"
    id = Column(Integer, primary_key = True)
    nome = Column(String, nullable= False)
    ano = Column(Integer, nullable= False)
    nota = Column(Float, nullable= False)
  
Base.metadata.create_all(engine)

def adicionar_anime(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    anime = Animes(nome=nome, ano=ano, nota=nota)
    session.add(anime)
    session.commit()
    session.close()

# adicionar_anime("Naruto", 2002, 8.5)
# adicionar_anime("One Piece", 1999, 9.5)

def atualiza_anime(id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Animes).filter_by(id=id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()

# atualiza_anime(1,'Naruto', 2002, 8.5)

def deletar_anime(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    anime = session.query(Animes).filter_by(id=id).first()
    if anime:
        session.delete(anime)
        session.commit()
    session.close()

deletar_anime(1)