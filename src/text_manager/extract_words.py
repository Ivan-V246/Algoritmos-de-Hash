def extract_words(path: str) -> list[str]:
    """
    Args:
        path (str): caminho do arquivo para ser lido
    Returns:
        list[str] | []: lista das palavras contidas no arquivo
    """
    try:
        # Abre o arquivo
        file = open(path, "r", encoding="UTF-8")
        
        list_words = file.read().lower().split() # Ler as palavras do arquivo e separa por espaco
        file.close() # Fecha o arquivo
    except Exception:
        return [] # Caso o arquivo nao exista
    
    return list_words # lista de palavras