# app.py

# Linha de importação: o Python vai procurar por 'estruturas_dados.py'
from estruturas import Node, UnorderedList, MinHeap, Tarefa

# Inicializar as estruturas de dados globais
tarefas_pendentes = MinHeap()
historico_tarefas_concluidas = UnorderedList()

def exibir_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar nova tarefa")
    print("2. Ver próxima tarefa (Prioritária)")
    print("3. Concluir próxima tarefa")
    print("4. Ver histórico de tarefas concluídas")
    print("5. Sair")
    print("------------------------------")

def adicionar_tarefa():
    print("--- Adicionar Nova Tarefa ---")
    descricao = input("Digite a descrição da tarefa: ")
    while True:
        try:
            prioridade = int(input("Digite a prioridade da Tarefa (1: Maxima prioridade; 5: Menor prioridade): "))
            if prioridade >= 1 and prioridade<= 5:
                print("Sucesso!")
                break
            else:
                print("A entrada deve ser entre 1 e 5!")
                continue
        except ValueError:
            print("Entrada inválida!")
            continue
    nova_tarefa = Tarefa(descricao, prioridade)
    tarefas_pendentes.insert(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

def ver_proxima_tarefa():
    # Lógica para ver a próxima tarefa
    pass

def concluir_proxima_tarefa():
    # Lógica para concluir a próxima tarefa
    pass

def ver_historico_tarefas():
    # Lógica para ver o histórico
    pass

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            ver_proxima_tarefa()
        elif opcao == '3':
            concluir_proxima_tarefa()
        elif opcao == '4':
            ver_historico_tarefas()
        elif opcao == '5':
            print("Saindo do Gerenciador de Tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()