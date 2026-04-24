import json

lista_tarefas = []

def salvar_dados():
    with open("dados.json", "w") as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4, ensure_ascii=False)
        print("\nSalvo no HD com sucesso!")

def carregar_dados():
    global lista_tarefas
    try:
        with open("dados.json", "r") as arquivo:
            lista_tarefas = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_tarefas = []
        print("\nCarregado no HD com sucesso!")

def adicionar_tarefa(descricao):

    tarefas = {
        "descricao": descricao,
        "concluida": False
    }
    lista_tarefas.append(tarefas)
    print(f"\n Tarefa '{descricao}' adicionada com sucesso!")

    
def listar_tarefas():
    print("\nLista de tarefas")
    if not lista_tarefas:
        print("\nA lista está vazia.")
    else:
        for indice, tarefa in enumerate(lista_tarefas, 1):
            status = "[X]" if tarefa["concluida"] else "[ ]"
            print(f"\nIndice:{indice}. {status}Tarefa:{tarefa['descricao']}") 

def concluir_tarefa(indice_usuario):
    try:
        indice = int(indice_usuario) - 1
        lista_tarefas[indice]["concluida"] = True
        print(f"\n Tarefa '{lista_tarefas[indice]['descricao']}' marcada como concluída!")
    
    except (IndexError, ValueError):
        print("\n Erro: Índice inválido! Verifique o número na lista.")

def apagar_tarefa(indice_usuario):
    try:
        indice = int(indice_usuario) - 1
        removida = lista_tarefas.pop(indice)
        print(f"\n Tarefa '{removida['descricao']}' removida!")
    except (IndexError, ValueError):
        print("\ Erro: Não foi possível apagar. Índice inexistente.")