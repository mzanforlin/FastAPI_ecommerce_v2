from database.database import engine  # Aqui você importa corretamente o engine
from models import base
from models.tb_usuarios import Usuarios

# Criar todas as tabelas
base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")
