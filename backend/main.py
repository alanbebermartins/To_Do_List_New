# Em um script ou no seu código principal

from app.crud.task_crud import create_task

# Tentar criar uma nova tarefa com título e descrição válidos
result = create_task(task_title="loja de ferramentas", task_description="Comprar ferramentas e material para conserto na lavanderia")
if isinstance(result, str):
    print(f"Erro: {result}")
else:
    print(f"Tarefa criada com sucesso! ID: {result.task_id}, Título: {result.task_title}, Descrição: {result.task_description}")

# Tentar criar uma nova tarefa com um título muito longo
result = create_task(task_title="Título muito longo que excede 20 caracteres", task_description="Comprar leite integral no supermercado")
if isinstance(result, str):
    print(f"Erro: {result}")
else:
    print(f"Tarefa criada com sucesso! ID: {result.task_id}, Título: {result.task_title}, Descrição: {result.task_description}")

# Tentar criar uma nova tarefa com uma descrição muito longa
result = create_task(task_title="Comprar leite", task_description="Descrição muito longa que excede 100 caracteres. Descrição muito longa que excede 100 caracteres. Descrição muito longa que excede 100 caracteres.")
if isinstance(result, str):
    print(f"Erro: {result}")
else:
    print(f"Tarefa criada com sucesso! ID: {result.task_id}, Título: {result.task_title}, Descrição: {result.task_description}")
