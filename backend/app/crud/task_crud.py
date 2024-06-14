from sqlalchemy.orm import Session
from app.models.task_models import Task
from app.database import SessionLocal

def create_task(task_title: str, task_description: str):
    db = SessionLocal()
    try:
        # Criar uma nova instância de Task
        new_task = Task(task_title=task_title, task_description=task_description)
        # Adicionar a nova instância ao banco de dados
        db.add(new_task)
        # Confirmar a transação
        db.commit()
        # Atualizar a instância para incluir o ID gerado pelo banco de dados
        db.refresh(new_task)
        return new_task
    finally:
        # Fechar a sessão do banco de dados
        db.close()
