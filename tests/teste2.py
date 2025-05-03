from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Coletar variáveis de ambiente
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')  # Se quiser usar schema depois

# Montar string de conexão
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?options=-c%20search_path={DB_SCHEMA}"


# Criar engine e base declarativa
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definir a tabela 'usuario'
class Usuario(Base):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': DB_SCHEMA}  # Definir o schema aqui
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

# Criar tabela
if __name__ == "__main__":
    try:
        Base.metadata.create_all(engine)
        print("✅ Tabela 'usuario' criada com sucesso.")
    except Exception as e:
        print("❌ Falha ao criar a tabela.")
        print(f"Erro: {e}")

    