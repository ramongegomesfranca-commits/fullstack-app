from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# 1. Defina o modelo de dados com Pydantic
class EmpresaBase(BaseModel):
    nome_empresa: str
    cnpj: str = Field(..., min_length=14, max_length=14, description="CNPJ deve conter apenas numeros é exatamente 14 numeros")
    tipo_relacionamento: str

# 2. Crie a rota POST usando o decorador
@app.post("/empresas/") 
async def cadastrar_empresa(empresa: EmpresaBase):
    return {"message": "Empresa cadastrada com sucesso!"}

@app.put("/empresas/") 
async def substituir_empresa(empresa: EmpresaBase):
    return {"message": "Empresa com dados corrigidos com sucesso!"}

@app.patch("/empresas/") 
async def atualizar_empresa(empresa: EmpresaBase):
    return {"message": "Empresa com dados atualizados com sucesso!"}
