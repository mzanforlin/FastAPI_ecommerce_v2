from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base  # Importa a base que você criou no __init__.py ou base.py
from models.user import User  # Importa a classe 'Usuarios' do arquivo tb_usuarios.py
from models.product import Product
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

# Criar engine e estabelecer conexão
db = create_engine(DATABASE_URL)

Session = sessionmaker()
session = Session()

Base.metadata.create_all(bind= db)
