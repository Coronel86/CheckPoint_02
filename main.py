import os
import time
from tarefas import adicionar_tarefa, listar_tarefas, apagar_tarefa, concluir_tarefa

TEMPO = 5 

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
            desc = input("Descrição da tarefa: ")
            adicionar_tarefa(desc)
            time.sleep(5)
        
        case "2":
            listar_tarefas()
            time.sleep(5)
        
        case "3":
            listar_tarefas() 
            idx = input("\nDigite o número da tarefa para concluir: ")
            concluir_tarefa(idx)
            time.sleep(5)
            
        case "4":
            listar_tarefas()
            idx = input("\nDigite o número da tarefa para apagar: ")
            apagar_tarefa(idx)
            time.sleep(5)
            
        case "5":
            print("Saindo... Obrigado por utilizar nosso sistema!")
            time.sleep(5)
            break
            
        case _:
            print("Opção inválida!")
            time.sleep(5)