from models.base import Base
from database import engine
import models  # Importa todas as tabelas registradas

# Criando todas as tabelas (User e Produto)
Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")