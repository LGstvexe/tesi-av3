# Implementação de uma Pilha (tipo LIFO) para simular o histórico de ações.

class HistoricoAcoes:
    def __init__(self):
        self.capacidade = 3              # capacidade inicial
        self.itens = [None] * self.capacidade
        self.tamanho = 0                  # topo da pilha

    # Função que dobra o tamanho da pilha caso ela fique cheia
    # Uma tentativa de simular o "realloc" em C.
    def redimensionar(self):
        capacidade_nova = self.capacidade * 2
        novo_array = [None] * capacidade_nova
        
        for i in range(self.tamanho):
            novo_array[i] = self.itens[i]

        self.itens = novo_array
        self.capacidade = capacidade_nova

    # Função para registrar (empilha) uma nova ação
    def add(self, acao):
        if self.tamanho == self.capacidade:
            self.redimensionar()

        self.itens[self.tamanho] = acao
        self.tamanho += 1

    # Função que desfaz (desempilha) a última ação registrada
    def undo(self):
        if self.tamanho == 0:
            raise Exception("Não há ações para serem desfeitas.")

        self.tamanho -= 1
        acao = self.itens[self.tamanho]

        # "limpar" a memória e mostrar apenas um valor Nulo.
        self.itens[self.tamanho] = None
        return acao


# ---------------------- SIMULAÇÃO -----------------------
# O comportamento esperado é tetnar desfazer as ações, mas por não existir nenhuma ação já feita, irá gerar uma exceção, retornando
# A mensagem de que "Não há ações para serem desfeitas."
try:
    historico = HistoricoAcoes()

    print(historico.undo())  # Não exisete ações feitas, logo gera uma exceção
    print(historico.itens) 
except Exception as e:
    print(e)

