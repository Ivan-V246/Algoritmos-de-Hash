from constants import PATH_FILE_NAMES
from math import sqrt

# Funcao que extrai os dados do arquivo e cria um hash com esse dados 
# Retorna os dados do Hash: colisoes, tamanho do array hash e fator de carga
def getDataHash(hashTable):
    with open(PATH_FILE_NAMES, 'r', encoding="UTF-8") as arquivo:
        nomes = arquivo.readlines()
        n = 0 
        for i in nomes:
            n += 1
            hashTable.put(i)
        
        #Abre o arquivo e adiciona cada uma das linhas a HashTable
        #Soma armazena a soma das colisões. Resp é um array de tuplas, que contém: [Posição, Colisões].
        resp = hashTable.numColisoes()
        x = [] # Eixo x
        y = [] # Eixo y
        
        for i in resp:
            #n += i[1] # Calcula a quantidade de elementos no hash
            x.append(i[0]) # quantidade de colunas no hash
            y.append(i[1]) # valores associados as colunas
            
                
        fator = hashTable.fator(n) # fator de carga do hash
        desvioPadrao = 0 # Erro de distribuicao hash
        excessoColisoes = 0
        isExcessoColisoes = 0
        
        # Calcula o erro de distribuicao
        for i in y:
            desvioPadrao += (i - fator)**2
            if i > fator:
                excessoColisoes += (i - fator)
                isExcessoColisoes += 1
        
        # Calculo do desvio padrao
        desvioPadrao = (desvioPadrao / len(x))
        desvioPadrao = sqrt(desvioPadrao)
        
        excessoColisoes = (excessoColisoes / isExcessoColisoes)
        
    return (x, y, fator, desvioPadrao, excessoColisoes)