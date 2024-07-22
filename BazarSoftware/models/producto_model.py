from sqlalchemy import Column, Integer, String
from . import Base

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    precio = Column(Integer)
