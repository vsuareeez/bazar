from modelos.venta_model import Venta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///bazar.db')
Session = sessionmaker(bind=engine)
session = Session()

def registrar_venta(id_producto, id_cliente, cantidad, total):
    nueva_venta = Venta(id_producto=id_producto, id_cliente=id_cliente, cantidad=cantidad, total=total)
    session.add(nueva_venta)
    session.commit()

def obtener_ventas():
    return session.query(Venta).all()
