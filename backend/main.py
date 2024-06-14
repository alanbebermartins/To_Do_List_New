# Em um script ou no seu código principal

from app.crud.task_crud import create_task

# Criar uma nova tarefa
new_task = create_task(task_title="Montar Cronograma", task_description="Montar o planejamento das tasks no jira, baseado no tamanho da equipe e tecnologias utlizadas")

print(f"Tarefa criada com sucesso! ID: {new_task.task_id}, Título: {new_task.task_title}, Descrição: {new_task.task_description}")
