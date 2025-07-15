# 📚 Gerenciador de Tarefas em Python

Este é um projeto de Gerenciador de Tarefas simples desenvolvido em Python, utilizando estruturas de dados como **Min-Heap (Heap Mínimo)** para gerenciar tarefas por prioridade e **Lista Encadeada** para manter um histórico de tarefas concluídas.

O objetivo principal deste projeto é demonstrar a aplicação prática das estruturas de dados em um cenário real ou simulado, conforme os requisitos da disciplina de Estrutura de Dados.

---

## 🎯 Objetivo Geral

Desenvolver uma aplicação que utilize, de forma significativa, as estruturas de dados estudadas na disciplina para resolver um problema real de gerenciamento de tarefas, priorizando a organização e a eficiência.

---

## ⚙️ Requisitos do Projeto Atendidos

* **Uso de Estruturas de Dados Obrigatórias:**
    * **Min-Heap:** Utilizado para armazenar e gerenciar as tarefas pendentes, garantindo que a tarefa com a **maior prioridade (menor valor numérico)** seja sempre acessível no topo.
    * **Lista Encadeada Não Ordenada:** Empregada para armazenar o histórico de tarefas que já foram concluídas, mantendo a ordem em que foram finalizadas.
* **Interface:** Atualmente, a interface é em modo texto (console). Uma interface gráfica básica está planejada para implementação futura.
* **Documentação Obrigatória:** Este `README.md` serve como parte da documentação inicial do projeto, explicando suas funcionalidades e como executá-lo.

---

## 🚀 Funcionalidades Implementadas

O gerenciador de tarefas atualmente oferece as seguintes funcionalidades no modo console:

1.  ### Adicionar Nova Tarefa
    Permite ao usuário inserir uma nova tarefa no sistema.
    * É solicitada a **descrição** da tarefa (texto livre).
    * É solicitada a **prioridade** da tarefa (um número inteiro de 1 a 5, onde 1 é a prioridade máxima e 5 é a prioridade mínima). O sistema valida a entrada para garantir que seja um número dentro do intervalo especificado.
    * A tarefa é adicionada ao **Min-Heap** de tarefas pendentes, sendo automaticamente organizada com base em sua prioridade.

2.  ### Ver Próxima Tarefa (Prioritária)
    Exibe a tarefa que possui a maior prioridade (menor valor numérico) entre as tarefas pendentes.
    * A tarefa é **apenas visualizada**, não sendo removida do sistema.
    * Se não houver tarefas pendentes, uma mensagem informativa é exibida.

3.  ### Concluir Próxima Tarefa
    Marca a tarefa de maior prioridade como concluída.
    * A tarefa com a maior prioridade é **removida** do Min-Heap de tarefas pendentes.
    * Esta tarefa é então **adicionada** à Lista Encadeada que armazena o histórico de tarefas concluídas.
    * Uma mensagem de confirmação informa qual tarefa foi finalizada.
    * Se não houver tarefas para concluir, uma mensagem informativa é exibida.

4.  ### Ver Histórico de Tarefas Concluídas
    Lista todas as tarefas que foram concluídas até o momento.
    * As tarefas são exibidas na ordem em que foram adicionadas ao histórico (o que, devido à implementação da Lista Encadeada, pode ser a ordem inversa de conclusão, dependendo de como o método `add` insere novos nós).
    * Se o histórico estiver vazio, uma mensagem informativa é exibida.

---

## 💻 Como Executar o Projeto

Para rodar este gerenciador de tarefas em seu ambiente local:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SeuUsuario/gerenciador-tarefas-python.git](https://github.com/SeuUsuario/gerenciador-tarefas-python.git)
    ```
    (Substitua `SeuUsuario` pelo seu nome de usuário no GitHub)

2.  **Navegue até o Diretório do Projeto:**
    ```bash
    cd gerenciador-tarefas-python
    ```

3.  **Estrutura de Arquivos:**
    Certifique-se de que você tem os seguintes arquivos na raiz do projeto:
    * `estruturas_dados.py` (contém as classes `Node`, `UnorderedList`, `MinHeap`, `Tarefa`)
    * `app.py` (contém a lógica principal do gerenciador e o menu de console)
    * `gui_app.py` (planejado para a futura interface gráfica)

4.  **Execute a Aplicação em Modo Console:**
    ```bash
    python app.py
    ```

    Isso iniciará o gerenciador de tarefas no seu terminal, exibindo o menu de opções.

---

## 👥 Contribuição

Este projeto foi desenvolvido como parte de um requisito acadêmico. Contribuições futuras podem incluir:

* Implementação da interface gráfica (Tkinter).
* Persistência de dados (salvar tarefas em um arquivo).
* Funcionalidades adicionais (editar tarefa, buscar tarefa, etc.).