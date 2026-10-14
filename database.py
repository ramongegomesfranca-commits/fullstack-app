from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# 1. A String de Conexão
# Usamos o sinal de '+' no lugar dos espaços no nome do Driver para a URL não quebrar.
DATABASE_URL = "mssql+pyodbc://@localhost\\SQLEXPRESS/CRM_DB?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"

# 2. O Motor (Engine)
engine = create_engine(DATABASE_URL)

# 3. A Sessão (SessionLocal)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. A Base (Classe mãe para transformar nossas tabelas SQL em código Python)
Base = declarative_base()

# Teste rápido de conexão
try:
    with engine.connect() as connection:
        print("Sucesso! O Python conseguiu entrar no SQL Server!")
except Exception as e:
    print(f"Erro ao conectar: {e}")

"""
Utilizei a Inteligencia Artificial do Google, utilizei ela como meu tech lead, para praticar e criar um sistema mais complexo, o código acima é um exemplo de como criar uma conexão com um banco de dados SQL Server usando SQLAlchemy e FastAPI, como eu não conhecia muito sobre essa tecnologia a IA achou por bem me passar a respostra pronta:

"Como seu Tech Lead, eu te dei esse bloco de código de bandeja por um motivo muito prático do mercado de trabalho: ninguém decora Connection Strings.
A sintaxe exata daquela URL (mssql+pyodbc://...driver=ODBC+Driver+17...) é o que chamamos de código boilerplate (configuração engessada). Não há lógica de programação ou regra de negócio para "adivinhar" ali, é puramente uma configuração de infraestrutura que até desenvolvedores seniores simplesmente copiam da documentação ou de projetos antigos. Se eu te deixasse tentar estruturar isso do zero, você perderia horas frustrantes brigando com versões de drivers do Windows e erros de digitação na URL."
"""