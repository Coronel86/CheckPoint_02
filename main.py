import os
import time
from tarefas import adicionar_tarefa, listar_tarefas, apagar_tarefa, concluir_tarefa, carregar_dados, salvar_dados

TEMPO = 5 

carregar_dados()

while True:
    
    os.system('cls' if os.name == 'nt' else 'clear')

  
    print("\n#### MENU ####")
    print("\n1- Adicionar")
    print("2- Listar")
    print("3- Concluir Tarefa")
    print("4- Apagar Tarefa")
    print("5- Sair")
    
    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            desc = input("\nDescrição da tarefa: ")
            adicionar_tarefa(desc)
            salvar_dados()
            time.sleep(TEMPO)
        
        case "2":
            listar_tarefas()
            time.sleep(8)
        
        case "3":
            listar_tarefas() 
            idx = input("\nDigite o número da tarefa para concluir: ")
            concluir_tarefa(idx)
            salvar_dados()
            time.sleep(TEMPO)
            
        case "4":
            listar_tarefas()
            idx = input("\nDigite o número da tarefa para apagar: ")
            apagar_tarefa(idx)
            time.sleep(TEMPO)
            
        case "5":
            print("\nSaindo... Obrigado por utilizar nosso sistema!")
            time.sleep(TEMPO)
            break
            
        case _:
            print("Opção inválida!")
            time.sleep(TEMPO)