from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Empresas(Base):
    __tablename__ = "empresas" 

    id_empresa = Column(Integer, primary_key=True, index=True)  # O ID original
    nome_empresa = Column(String(255), nullable=False)
    cnpj = Column(String(14), unique=True, nullable=True)
    tipo_relacionamento = Column(String(50), nullable=True)
            
class Representantes(Base):
    __tablename__ = "representantes"

    id_representante = Column(Integer, primary_key=True, index=True)
    id_empresa = Column(Integer,  ForeignKey('empresas.id_empresa'), nullable=False)
    nome_representante = Column(String(100), nullable=False)
    telefone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)


class Projetos(Base):
    __tablename__ = "projetos"

    id_projeto = Column(Integer, primary_key=True, index=True)
    id_empresa = Column(Integer, ForeignKey('empresas.id_empresa'), nullable=False)
    nome_evento = Column(String(100), nullable=False)
    data_montagem = Column(Date)
    data_evento_inicio = Column(Date)
    data_evento_termino = Column(Date)
    data_desmontagem = Column(Date)
    status_funil = Column(String(100))