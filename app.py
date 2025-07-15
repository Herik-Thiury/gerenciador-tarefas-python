# Linha de importação.
from estruturas import Node, UnorderedList, MinHeap, Tarefa

# Inicializador das estruturas.
tarefas_pendentes = MinHeap()
historico_tarefas_concluidas = UnorderedList()

# Função para dashboard de escolhas.
def exibir_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar nova tarefa")
    print("2. Ver próxima tarefa (Prioritária)")
    print("3. Concluir próxima tarefa")
    print("4. Ver histórico de tarefas concluídas")
    print("5. Sair")
    print("------------------------------")

#Método para adicionar uma nova tarefa que será organizada no min heap
def adicionar_tarefa():
    print("\n--- Adicionar Nova Tarefa ---")
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

#Método para ver próxima tarefa por ordem de prioridade.
def ver_proxima_tarefa():
    print("\n--- Próxima Tarefa Prioritária ---")
    if tarefas_pendentes.current_size == 0:
        print("Não há tarefas Pendentes!")
    else:
        proxima_tarefa = tarefas_pendentes.heap_list[1]
        print(proxima_tarefa)

#Método para concluir próxima tarefa por ordem de prioridade.
def concluir_proxima_tarefa():
    print("\n--- Concluir Próxima Tarefa ---")
    if tarefas_pendentes.current_size == 0:
        print("Não há tarefas pendentes!")
    else:
        tarefa_concluida = tarefas_pendentes.delete_min()
        historico_tarefas_concluidas.add(tarefa_concluida)
        print(f"A tarefa {tarefa_concluida} foi concluída!")

#Método para ver histórico de tarefas concluídas
def ver_historico_tarefas():
    print("\n--- Histórico de Tarefas Concluídas ---")
    if historico_tarefas_concluidas.isEmpty():
        print("Nenhuma tarefa foi concluída ainda")
    else:
        atual = historico_tarefas_concluidas.head
        while atual is not None:
            print(atual.getData())
            atual = atual.getNext()

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