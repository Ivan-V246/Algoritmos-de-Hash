from constants import PATH_FILE_NAMES

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
        x = []
        y = []
        n = 0
        for i in resp:
            n += i[1]
            x.append(i[0])
            y.append(i[1])
            
    return (x,y, hashTable.fator(n))