class Node: #Definição da classe Node
    
    #Contém: um valor armazenado nesse Nó e um ponteiro pro próximo Node
    def __init__(self,valor):
        self.valor = valor
        self.prox = None