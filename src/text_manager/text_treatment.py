import re # biblioteca para criar expressoes regulares
import unicodedata # modulo de caracteres do python

# Função que remove acentos
def remover_acentos(txt: str) -> str:
    """
    Remove os acentos de uma string

    Args:
        txt (str): texto que se deseja extrair os acentos

    Returns:
        str: string sem acentos
    """
    # Separa as letras dos acentos: á = 'a', '´'
    decomposto = unicodedata.normalize("NFD", txt)
    
    # Remove os caracteres de acento (categoria Mn = acentos)
    # unicodedata.category retorna a categoria do caracter c
    # se for diferente de Mn implica que nao e um acento
    return "".join([c for c in decomposto if unicodedata.category(c) != "Mn"])

def clear_arq_text(path_read: str) -> list[str]:
    """
    Cria um lista de palavras contidas em um arquivo tirando simbolos e acentos.

    Args:
        path_read (str): caminho do arquivo que se deseja limpar

    Returns:
        list[str]: lista de palavras contidas no arquivo, tirando acentos e simbolos
    """
    try:
        # Abre o arquivo
        with open(path_read, "r", encoding="utf-8") as file:
            texto = file.read()

        # Remove símbolos e números, utilizando expressao regular
        # Basicamente deixa apenas letras
        texto_limpo = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto) 

        # Remove acentos
        texto_sem_acentos = remover_acentos(texto_limpo)
        
        # Deixa em minusculo as palavras 
        texto_sem_acentos = texto_sem_acentos.lower()

        return texto_sem_acentos.split() # Retorna lista de palavras limpas
    
    except Exception:
        return [''] # Caso nao consiga ler o arquivo


def clear_arq_save(path_read: str, path_write: str) -> None:
    """
    Ler um arquivo e retira simbolos e acentos e salva o conteudo em outro aquivo
    
    Args:
        path_read (str): caminho do arquivo que deve ser lido
        path_write (str): caminho para salvar o resultado
    """
    
    try:
        # Abre o arquivo
        with open(path_read, "r", encoding="utf-8") as file:
            texto = file.read()

        # Remove símbolos e números, utilizando expressao regular
        # Basicamente deixa apenas letras
        texto_limpo = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto) 

        # Remove acentos
        texto_sem_acentos = remover_acentos(texto_limpo)
        
        # Deixa em minusculo as palavras 
        texto_sem_acentos = texto_sem_acentos.lower()

        # Salva no novo arquivo
        with open(path_write, "w", encoding="utf-8") as file:
            file.write(texto_sem_acentos)
        print("Arquivo salvo")
        
    except Exception:
        print("Error ao abrir o aquivo")
