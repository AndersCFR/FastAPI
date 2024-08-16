from fastapi import FastAPI, Depends, Htt
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import logging


app = FastAPI()

# Configurar el sistema de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurar SQLAlchemy
DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()


class NewTable(Base):
    __tablename__ = "newtable"
    id = Column(Integer, index=True, primary_key=True)
    nombre = Column(String, index=False)
    saldo = Column(Float(precision=8))
    # Añadir más columnas según sea necesario


# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los datos de la tabla
@app.get("/data/")
def read_data(skip: int = 0, limit: int = 10, saldo_min: float = 0.00 ,db: Session = Depends(get_db)):
    #for item in data:
        #logger.info(f"Nombre: {item.nombre}, Saldo: {item.saldo}")
     # Construir la consulta
     # Construir la consulta
    query = db.query(NewTable)

    # Aplicar filtro si se proporciona el parámetro saldo_min
    if saldo_min is not None:
        query = query.filter(NewTable.saldo >= saldo_min)

    # Aplicar offset y limit
    query = query.offset(skip).limit(limit)

    # Obtener los resultados
    data = query.all()

    return data