import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", backref="usuario")

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    terreno = Column(String(250))
    favoritos = relationship("Favorito", backref="planeta")

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    especie = Column(String(250), nullable=False)
    genero = Column(String(250))
    favoritos = relationship("Favorito", backref="personaje")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)  
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True) 

    usuario = relationship("Usuario", backref="favoritos")
    planeta = relationship("Planeta", backref="favoritos")
    personaje = relationship("Personaje", backref="favoritos")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
