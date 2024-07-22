from modelos.producto_model import Producto
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///bazar.db')
Session = sessionmaker(bind=engine)
session = Session()

def agregar_producto(nombre, precio):
    nuevo_producto = Producto(nombre=nombre, precio=precio)
    session.add(nuevo_producto)
    session.commit()

def obtener_productos():
    return session.query(Producto).all()
