from sqlalchemy.orm import Session
from app.models.task_models import Task
from app.database import SessionLocal

def create_task(task_title: str, task_description: str):
    # Verificar o comprimento do título da tarefa
    title_error = None
    description_error = None
    
    if len(task_title) > 20:
        title_error = "O título da tarefa deve possuir no máximo 20 caracteres"
    
    # Verificar o comprimento da descrição da tarefa
    if len(task_description) > 100:
        description_error = "A descrição da tarefa deve possuir no máximo 100 caracteres"
    
    # Se houver qualquer erro, retornar as mensagens de erro
    if title_error and description_error:
        return f"{title_error} e {description_error}"
    elif title_error:
        return title_error
    elif description_error:
        return description_error
    
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

