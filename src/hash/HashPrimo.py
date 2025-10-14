from constants import PATH_FILE_NAMES

class Node: #Definição da classe Node
    
    #Contém: um valor armazenado nesse Nó e um ponteiro pro próximo Node
    def __init__(self,valor):
        self.valor = valor
        self.prox = None

class HashTablePrimo: #Definição da classe HashTable
    
    #Contém: Um tamanho de possíveis posições M, um array pra guardar as 
    #listas de cada posição e um array pra guardar as colisões de cada posição.

    def __init__(self, M):
        self.M = M
        self.table = [None] * M
        self.colisoes = [0] * M
    
    #Método que insere um novo item na HashTable, adicionando-o na posição indicada por seu Hash
    def put(self, nome):
        temp = Node(nome)
        pos = self._hash(nome)
        if self.table[pos] == None:
            self.table[pos] = temp # type: ignore
        else:
            temp.prox = self.table[pos]
            self.table[pos] = temp # type: ignore
            self.colisoes[pos] +=1

    #Método que retorna uma lista de tuplas, contendo a letra equivalente e a quantidade de colisões pra aquela letra.
    def numColisoes(self):
        resp = [(0, 0)] * self.M
        for i in range(self.M):
            resp[i] = (i, self.colisoes[i])
        return resp
    
    #Método que retorna o Hash de cada item. Nesse caso o Hash é o padrão da liguagem.
    def _hash(self, nome):
        h = 0
        for c in nome:
            h = (31 * h + ord(c)) % self.M
        return h 
    
    #Método que exibe todos as posições de hash e os elementos presentes em cada uma.
    def show(self):
        for i in range(self.M):
            print(f"{i} -> ")
            aux = self.table[i]
            while(aux != None):
                print(aux.valor)
                aux = aux.prox

    #Retorna o fator de carga da HashTable atual ao passar a quantidade de elementos inseridos
    def fator(self, n):
        return n/self.M

def resultPrimo():
    Tabela = HashTablePrimo(26) #Cria a estrutura de HashTable, definindo as posições
    with open(PATH_FILE_NAMES, 'r', encoding="UTF-8") as arquivo:
        sla = arquivo.readlines()
        for i in sla:
            Tabela.put(i)
        
        #Abre o arquivo e adiciona cada uma das linhas a HashTable
        #Soma armazena a soma das colisões. Resp é um array de tuplas, que contém: [Posição, Colisões].
        resp = Tabela.numColisoes()
        x = []
        y = []
        n = 0
        for i in resp:
            n += i[1]
            x.append(i[0])
            y.append(i[1])
            
    return (x,y, Tabela.fator(n))