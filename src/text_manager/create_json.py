# Cria os JSON com os dados
import json
from pathlib import Path

def create_json(algoritmo: str, quantidade: int, tempo_exec: float, save_dir: Path):
    """
    Cria um arquivo JSON com os dados de execução de um algoritmo.

    Args:
        algoritmo (str): Nome do algoritmo.
        quantidade (int): Quantidade de palavras processadas.
        tempo_exec (float): Tempo de execução em segundos.
    """
    
    # Json dos dados
    dado = {
        "algoritmo": algoritmo,
        "quantidade_palavras": quantidade,
        "tempo": tempo_exec
    }
    
    # path para salvar
    save = save_dir / f"{algoritmo}_teste.json"
    content = [] # conteudo
    
    # Abre no modo leitura 
    with open(save, "r", encoding="UTF-8") as file:
        dados = json.load(file) # ler todos os dados do arquivo
        for js in dados:
            content.append(js)
            
        content.append(dado) # Adiciona o novo valor
        
    # Abre no modo escrita, para apagar o que tinha antes
    with open(save, "w", encoding="UTF-8") as file:
        # Escreve o conteudo novo junto com o anterior
        json.dump(content, file, indent=4, ensure_ascii=False) 