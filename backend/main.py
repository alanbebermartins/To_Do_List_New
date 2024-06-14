# Em um script ou no seu código principal

from app.crud.task_crud import create_task

# Tentar criar uma nova tarefa com título e descrição válidos
result = create_task(task_title="Reuniao na escola dos filhos", task_description="Reuniao da escola para conversar a respeito sobre o pessimo comportamento que o ricardo teva na sala de aula com o professor, pois ficou respondendo de forma mal educada.")
if isinstance(result, str):
    print(f"Erro: {result}")
else:
    print(f"Tarefa criada com sucesso! ID: {result.task_id}, Título: {result.task_title}, Descrição: {result.task_description}")

# Tentar criar uma nova tarefa com um título muito longo
result = create_task(task_title="Título muito longo que excede 20 caracteres", task_description="levar o carro na consecionaria para fazer a revisao de 60000 km")
if isinstance(result, str):
    print(f"Erro: {result}")
else:
    print(f"Tarefa criada com sucesso! ID: {result.task_id}, Título: {result.task_title}, Descrição: {result.task_description}")

# Tentar criar uma nova tarefa com uma descrição muito longa
result = create_task(task_title="Manutençao do carro", task_description="Descrição muito longa que excede 100 caracteres. Descrição muito longa que excede 100 caracteres. Descrição muito longa que excede 100 caracteres.")
if isinstance(result, str):
    print(f"Erro: {result}")
else:
    print(f"Tarefa criada com sucesso! ID: {result.task_id}, Título: {result.task_title}, Descrição: {result.task_description}")

# Tentar criar uma nova tarefa com título e descrição muito longos
result = create_task(task_title="Título muito longo que excede 20 caracteres", task_description="Descrição muito longa que excede 100 caracteres. Descrição muito longa que excede 100 caracteres. Descrição muito longa que excede 100 caracteres.")
if isinstance(result, str):
    print(f"Erro: {result}")
else:
    print(f"Tarefa criada com sucesso! ID: {result.task_id}, Título: {result.task_title}, Descrição: {result.task_description}")


