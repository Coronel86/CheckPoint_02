lista_tarefas = []

def adicionar_tarefa(descricao):

    tarefa = {
        "descricao": descricao,
        "concluida": False
    }
    lista_tarefas.append(tarefa)
    print(f"\n Tarefa '{descricao}' adicionada com sucesso!")

    for tarefa in lista_tarefas


def listar_tarefas():
    print("Lista de tarefas")
    if lista_tarefas:
        print("A lista está vazia.")
    else:
        for tarefa in lista_tarefas:
            print(f"executar {tarefa}['descricao']")  