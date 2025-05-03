from sqlalchemy import create_engine
#from models import base
from models.base import Base  # Importa a base que você criou no __init__.py ou base.py
from models.tb_usuarios import Usuarios  # Importa a classe 'Usuarios' do arquivo tb_usuarios.py
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
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criar engine e estabelecer conexão
engine = create_engine(DATABASE_URL)

# Criar as tabelas no banco de dados
if __name__ == "__main__":
    try:
        Base.metadata.create_all(engine) # Isso cria todas as tabelas que foram definidas com a Base
        print("✅ Tabela 'Usuarios' criada com sucesso.")
    except Exception as e:
        print("❌ Falha ao criar a tabela.")
        print(f"Erro: {e}")
