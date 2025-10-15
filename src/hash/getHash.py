from constants import PATH_FILE_NAMES
from math import sqrt

# Funcao que extrai os dados do arquivo e cria um hash com esse dados 
# Retorna os dados do Hash: colisoes, tamanho do array hash e fator de carga
def getDataHash(hashTable):
    with open(PATH_FILE_NAMES, 'r', encoding="UTF-8") as arquivo:
        sla = arquivo.readlines()
        for i in sla:
            hashTable.put(i)
        
        #Abre o arquivo e adiciona cada uma das linhas a HashTable
        #Soma armazena a soma das colisões. Resp é um array de tuplas, que contém: [Posição, Colisões].
        resp = hashTable.numColisoes()
        x = [] # Eixo x
        y = [] # Eixo y
        n = 0 # Quantidade de elementos
        
        for i in resp:
            n += i[1] # Calcula a quantidade de elementos no hash
            x.append(i[0]) # quantidade de colunas no hash
            y.append(i[1]) # valores associados as colunas
            
                
        fator = hashTable.fator(n) # fator de carga do hash
        errorDistHash = 0 # Erro de distribuicao hash
        
        # Calcula o erro de distribuicao
        for i in y:
            if i > fator:
                errorDistHash += (i - fator)**2
        
        # Calculo do desvio padrao
        errorDistHash = (errorDistHash / len(x))
        errorDistHash = sqrt(errorDistHash)
        
    return (x, y, fator, errorDistHash)