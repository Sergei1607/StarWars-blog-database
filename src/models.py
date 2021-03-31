import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=True)
    orbital_period = Column(Integer, nullable=True)
    diameter = Column(Integer, nullable=True)
    climate = Column(String(250), nullable=True)
    gravity = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    surface_water = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)


class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hair_color = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    birth_year = Column(Integer, nullable=True)
    gender = Column(String(250), nullable=True)

class Usuario(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    personaje_id = Column(Integer, ForeignKey('personajes.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')