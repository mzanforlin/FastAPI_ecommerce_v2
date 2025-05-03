from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

print('###### Teste de credenciais######')

print(DB_HOST)
print(DB_PORT)
print(DB_NAME)
print(DB_USER)
print(DB_PASS)
print(DB_SCHEMA)

print('#########################')


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?options=-c%20search_path={DB_SCHEMA}"



try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("✅ Conexão bem-sucedida com o banco de dados!")
    connection.close()
except Exception as e:
    print("❌ Falha ao conectar no banco de dados.")
    print(f"Erro: {e}")
