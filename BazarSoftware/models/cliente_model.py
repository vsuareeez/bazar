from sqlalchemy import Column, Integer, String
from . import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    direccion = Column(String(100))
