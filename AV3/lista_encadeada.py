class NoTarefa:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeadaTarefas:
    def __init__(self):
        self.cabeca = None

    def inserir_inicio(self, dado):
        novo_no = NoTarefa(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        print(f"-> Tarefa '{dado['titulo']}' inserida.")

    def listar_tarefas(self):
        atual = self.cabeca 
        if atual is None:
            print("A lista de tarefas está vazia.")
            return

        ordem = 1
        while atual is not None:
            titulo = atual.dado.get("titulo", "N/A")
            prioridade = atual.dado.get("prioridade", "N/A")
            print(f"[{ordem}] Nome da Tarefa: {titulo} | Prioridade: {prioridade}")
            
            atual = atual.proximo
            ordem += 1

    def bubble_sort_tarefas(self):
        if self.cabeca is None:
            return
        
        trocou = True
        
        while trocou:
            trocou = False
            atual = self.cabeca

            while atual.proximo is not None:
                prox = atual.proximo

                if atual.dado["prioridade"] > prox.dado["prioridade"]:
                    atual.dado, prox.dado = prox.dado, atual.dado
                    trocou = True

                atual = atual.proximo

# --- EXECUÇÃO DE TESTE ---
# Basicamente serão inseridas as tarefas e seu nível de prioridade, com o 1 sendo o maior nível de prioridade.
# Antes do uso do Bubble Sort, o comportamento esperado é que as tarefas sejam inseridas por ordem de menor prioridade e após isso, seja ordenada de forma que respeite
# A ordem de prioridade explicada anteriormente.
gerenciador = ListaEncadeadaTarefas()

# Inserindo tarefas
gerenciador.inserir_inicio({"titulo": "Análise de Dados Clientes", "prioridade": 3})
gerenciador.inserir_inicio({"titulo": "Revisão do Relatório Mensal", "prioridade": 2})
gerenciador.inserir_inicio({"titulo": "Configuração de Alerta", "prioridade": 1})

# Antes da ordenação
print("\nANTES DO BUBBLE SORT:\n")
gerenciador.listar_tarefas()

# Ordenação
gerenciador.bubble_sort_tarefas()

# Depois da ordenação
print("\nDEPOIS DO BUBBLE SORT:\n")
gerenciador.listar_tarefas()