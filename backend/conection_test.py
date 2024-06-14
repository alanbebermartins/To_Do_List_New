from app.database import get_db
from sqlalchemy import text  # Importe text do SQLAlchemy

def test_connection():
    db = next(get_db())
    try:
        result = db.execute(text("SELECT 1"))  # Use text() para declarar a expressão SQL
        print("Conexão com o banco de dados estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()
