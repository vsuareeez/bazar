from sqlalchemy import Column, Integer, String
from . import Base

class Cajero(Base):
    __tablename__ = 'cajeros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    turno = Column(String(50))
