from ting_file_management.abstract_queue import AbstractQueue


# Definição da classe Queue que herda de AbstractQueue
class Queue(AbstractQueue):
    def __init__(self):
        # Inicializa a fila como uma lista vazia
        self._fila = list()
        # Inicializa o tamanho da fila como zero
        self._tamanho = 0

    def __len__(self):
        # Retorna o tamanho da fila
        return self._tamanho

    def __str__(self):
        # Cria uma string vazia para armazenar os elementos da fila
        elem_fila = ""
        # Itera sobre os elementos na fila
        for elem_atual in range(len(self._fila)):
            # Obtém o valor do elemento atual
            value = self._fila[elem_atual]
            # Converte o valor para uma string e adiciona à string de itens
            elem_fila += str(value)
            # Se não for o último elemento, adiciona uma vírgula e um espaço
            if elem_atual + 1 < len(self._fila):
                elem_fila += ", "

        # Retorna a representação em string da fila
        return "Queue(" + elem_fila + ")"

    def enqueue(self, value):
        # Adiciona um elemento ao final da fila
        self._fila.append(value)
        # Incrementa o tamanho da fila
        self._tamanho += 1

    def dequeue(self):
        # Remove e retorna o primeiro elemento da fila
        primeiro_elemento = self._fila.pop(0)
        # Decrementa o tamanho da fila
        self._tamanho -= 1
        # Retorna o elemento removido
        return primeiro_elemento

    def search(self, index):
        # Verifica se o índice é inválido ou inexistente
        if index < 0 or index > self._tamanho - 1:
            # Gera uma exceção de índice inválido ou inexistente
            raise IndexError("Índice Inválido ou Inexistente")
        try:
            # Tenta acessar o elemento no índice fornecido
            return self._fila[index]
        except Exception:
            # Gera uma exceção de índice inválido ou inexistente se ocorrer um erro
            raise IndexError("Índice Inválido ou Inexistente")
