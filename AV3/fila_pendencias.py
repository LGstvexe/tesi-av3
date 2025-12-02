# Implementação de uma Fila (tipo FIFO) para simular as tarefas pendentes.

class FilaPendencias:
    def __init__(self):
        self.capacidade = 5              # capacidade inicial da fila
        self.itens = [None] * self.capacidade
        self.tamanho = 0                 # quantidade de elementos
        self.inicio = 0                  # índice do primeiro elemento
        self.fim = 0                     # índice onde o próximo será inserido

    # Função que dobra o tamanho da pilha caso ela fique cheia
    # Uma tentativa de simular o "realloc" em C.
    def redimensionar(self):
        capacidade_nova = self.capacidade * 2
        novo_array = [None] * capacidade_nova

        # Basicamente copia os elementos na ordem correta
        for i in range(self.tamanho):
            novo_array[i] = self.itens[(self.inicio + i) % self.capacidade]

        # Troca arrays e atualiza os "ponteiros"
        self.itens = novo_array
        self.capacidade = capacidade_nova
        self.inicio = 0
        self.fim = self.tamanho

    def enqueue(self, tarefa):
        # Se estiver cheia, a capacidade é aumentada.
        if self.tamanho == self.capacidade:
            self.redimensionar()

        # Adiciona ao final
        self.itens[self.fim] = tarefa

        # Avança o ponteiro do fim
        self.fim = (self.fim + 1) % self.capacidade

        self.tamanho += 1

    def dequeue(self):
        # Caso a fila esteja vazia, retorna um erro
        if self.tamanho == 0:
            raise Exception("Nenhuma tarefa pendente.")

        # Pega o elemento do início
        tarefa = self.itens[self.inicio]

        # "limpar" a memória e mostrar apenas um valor Nulo.
        self.itens[self.inicio] = None

        # Avanaça o ponteiro do início
        self.inicio = (self.inicio + 1) % self.capacidade

        self.tamanho -= 1
        return tarefa

# ----------------- EXEMPLO DE USO -----------------

try:
    fila = FilaPendencias()

    fila.enqueue("Desenvolvimento de Dashboard")
    fila.enqueue("Modelagem de dados")
    fila.enqueue("Atualizar Logs")

    print("Tarefa Concluída:", fila.dequeue()) 
    print("Tarefa Concluida:", fila.dequeue())
except Exception as e:
    print(e)
