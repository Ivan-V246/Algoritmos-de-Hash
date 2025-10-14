# Trabalho em Grupo — Estrutura de Dados: Teste dos algoritmos de ordenação
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-17-blue?logo=cplusplus&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-GUI-brightgreen?logo=qt&logoColor=white)
![pybind11](https://img.shields.io/badge/pybind11-C%2B%2B%20Bindings-blue?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Gráficos%202D-red?logo=plotly&logoColor=white)
![Git](https://img.shields.io/badge/Git-Versionamento-orange?logo=git&logoColor=white)


Este projeto tem como objetivo **testar algoritmos de ordenação**, com foco na **prática de conceitos de Estrutura de Dados**, principalmente os **algoritmos de ordenação**, implementadas com **a linguagem C++**.

---

## 👨‍💻 Integrantes do Grupo
- **Gleidson Luan Sena Alves**  
- **Ivan Vitor Dias de Oliveira**  
- **Antonio Gemesson Sousa de Oliveira**

---

## 🛠️ Ferramentas Utilizadas
- **[Python](https://www.python.org/)** — linguagem de programação principal do projeto.  
- **[C++](https://devdocs.io/cpp/)** - linguagem usada para implementar os algoritmos de ordenação.
- **[Pybind11](https://pybind11.readthedocs.io/en/stable/)** - biblioteca python que facilita a criação de pacotes escritos em c++ para python.
- **[Setuptools](https://setuptools.pypa.io/en/latest/)** - biblioteca de suporte para o Pybind11, responsável pelo empacotamento e geração dos módulos compilados, .so no Linux e .pyd no Windows.
- **[PySide6](https://doc.qt.io/qtforpython-6/)** - biblioteca para construção de interfaces gráficas (GUI).  
- **[Matplotlib](https://matplotlib.org/stable/users/index.html)** - biblioteca usada para criar os gráficos.
- **[Git](https://git-scm.com/)** — versionamento e controle do código.  
---

## ⚙️ Funcionalidades
- **Gráfico de desempenho** - Ver gráfico de desempenho de cada algoritmo de ordenação:
    - Bubble Sort
    - Selection Sort
    - Insertion Sort
    - Shell Sort
    - Merge Sort
    - Quick Sort
    - Heap Sort
- **Realizar teste de algoritmo** - Realiza 5 testes com o algoritmo escolhido e o arquivo com palavras para ser ordenado. Mostrando no final a média do tempo de CPU gasto.
- **Comparação de algoritmos** - Compara dois algoritmos por tempo de CPU gasto na execução.  
---
## Como testar
Com python instalado:
```bash
git clone "https://github.com/AbstractGleidson/AlgoritmosOrdenacao.git"
cd AlgoritmosOrdenacao
pip install -r requirements.txt
cd src 
python main.py
```