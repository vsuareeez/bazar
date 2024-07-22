from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
from .producto_model import Producto
from .cliente_model import Cliente
from .cajero_model import Cajero

class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('productos.id'))
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    id_cajero = Column(Integer, ForeignKey('cajeros.id'))

    producto = relationship(Producto)
    cliente = relationship(Cliente)
    cajero = relationship(Cajero)
