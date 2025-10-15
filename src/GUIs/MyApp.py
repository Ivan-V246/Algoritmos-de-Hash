# Cria de fato a interface da aplicacao
# Para futuras modificacao, e interessante implementar um esquema de navegacao usando QStackedWidget
from PySide6.QtWidgets import QMainWindow, QWidget, QCheckBox, QListWidget, QStyle, QFileDialog, QDialog, QProgressBar # Principais widgets
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QListView, QAbstractItemView
from PySide6.QtGui import QFont, QIcon, QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QThread, Signal
from .widgets.smallWidgets import buttonMainMenu
from constants import ICON2_PATH, WINDOW_HEIGTH, WINDOW_WIDTH
from .Charts.generateCharts import MplCanvas
from matplotlib.ticker import ScalarFormatter
from datetime import datetime
import sys
from hash.HashLetter import resultLetter
from hash.HashPython import resultPython
from hash.HashPrimo import resultPrimo

# Herda QMainWindow para ter acesso a alguns componentes da janela em si, como title e icon 
class MyWindow(QMainWindow):
    finished = Signal(float) # Sinal que terminou a execucao do algorítimo no caso de um teste de ordenacao
    
    def __init__(self):
        super().__init__()
        self.errorMessage = None # Gerencia a messagem de erro na leitura de dado, se ela deve ser exibida ou nao
        self.fileName = None # Gerencia o arquivo que será enviado para ordenar 
        self.algorithm = None # Gerencia o algorítmo escolhido para ordenação
        self.loading_dialog = None  # Gerencia o diálogo de carregamento
        self.autoTeste = None # Gerencia o teste automatico


        self.setWindowTitle("Implementações Hash")
        self.setFixedSize(WINDOW_HEIGTH, WINDOW_WIDTH)
        self.setWindowIcon(QIcon(ICON2_PATH)) # Troca o icone da janela
        self.showMainMenu()  # Mostra a primeira janela


    # Renderiza o menu principal da aplicacao 
    def showMainMenu(self):
        CENTER = Qt.AlignmentFlag.AlignCenter # Cria um centralizacao 

        widget = QWidget() # Widget generico
        layout = QVBoxLayout() # Box vertical
        
        layout.setContentsMargins(0, 30, 0, 30) # Mergin no final e no inicio

        # Metodologia 1
        button_view_graph = buttonMainMenu("Metodologia 1")
        button_view_graph.clicked.connect(self.showHashLetter) # Adiciona funcao para esse botao
        
        # Metodologia 2
        button_compare_algorithms = buttonMainMenu("Metodologia 2")
        button_compare_algorithms.clicked.connect(self.showHashPython) # Adiciona funcao para esse botao
        
        # Metodologia 3 
        button_metodologia3 = buttonMainMenu("Metodologia 3")
        button_metodologia3.clicked.connect(self.showHashPrimo) 
        
        # Metodologia 3 
        button_metodologia4 = buttonMainMenu("Metodologia 4")
        button_metodologia4.clicked.connect(self.showHashPares) 
        
        # Sai da aplicacao
        button_report = buttonMainMenu("Sair")
        button_report.clicked.connect(self.exitAplication) # Adiciona funcao para esse botao

        # Adiciona os botoes no layout
        layout.addWidget(button_view_graph, alignment=CENTER)
        layout.addWidget(button_compare_algorithms, alignment=CENTER)
        layout.addWidget(button_metodologia3, alignment=CENTER)
        layout.addWidget(button_metodologia4, alignment=CENTER)
        layout.addWidget(button_report, alignment=CENTER)
        
        widget.setLayout(layout) # Adiciona o layout no widget generico

        self.setCentralWidget(widget)  # Renderiza esse widget generico que foi criado 

    # Primeira implementacao do hash usando uma os index como as letras do alfabeto
    def showHashLetter(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        # widget e layout da tela
        widget = QWidget()
        layout = QVBoxLayout()

        # Seletor de Algoritmo para escolher quem vai ser usado
        label_select = QLabel("Metodologia 1")
        label_select.setFont(FONT)

        # Dados 
        x, y, fator = resultLetter()

        # Associa letras com o index, usando os valores da tabela ASCII
        labels = [chr(65 + i) for i in range(len(x))]

        # Encontra o maior e o menor número de colisões
        max_y = max(y)
        min_y = min(y)

        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.clear()

        # Título e rótulos
        self.canvas.axes.set_title("Histograma", fontsize=16)
        self.canvas.axes.set_xlabel("Letras (A - Z)")
        self.canvas.axes.set_ylabel("Quantidade de colisões")

        # Configurações visuais
        self.canvas.figure.tight_layout()
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.05, y=0.1)

        # Cores condicionais
        colors = []
        for valor in y:
            if valor == max_y:
                colors.append("tomato")       # vermelho para o maior valor
            elif valor == min_y:
                colors.append("limegreen")    # verde para o menor valor
            else:
                colors.append("skyblue")      # padrão

        # Plota o histograma com cores personalizadas
        self.canvas.axes.bar(labels, y, color=colors, edgecolor='black')

        # Linha do fator de carga
        self.canvas.axes.axhline(y=fator, color='red', linestyle='--', label="fator de carga")

        # Legenda
        self.canvas.axes.legend(loc='upper left')

        # Renderiza
        self.canvas.draw()

        # Botão para voltar pro menu principal
        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(200, 40)
        button_back.clicked.connect(self.showMainMenu)

        # Adiciona os botões e o gráfico no layout do widget
        layout.addWidget(label_select, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.canvas)
        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(20, 0, 20, 40)

        widget.setLayout(layout)
        self.setCentralWidget(widget)  # Renderiza na tela o widget criado

    # Segunda Metodologia
    def showHashPython(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        # widget e layout da tela
        widget = QWidget()
        layout = QVBoxLayout()

        # Seletor de Algoritmo para escolher quem vai ser usado
        label_select = QLabel("Metodologia 1")
        label_select.setFont(FONT)

        # Dados 
        x, y, fator = resultPython()

        # Associa letras com o index, usando os valores da tabela ASCII
        labels = [chr(65 + i) for i in range(len(x))]

        # Encontra o maior e o menor número de colisões
        max_y = max(y)
        min_y = min(y)

        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.clear()

        # Título e rótulos
        self.canvas.axes.set_title("Histograma", fontsize=16)
        self.canvas.axes.set_xlabel("Letras (A - Z)")
        self.canvas.axes.set_ylabel("Quantidade de colisões")

        # Configurações visuais
        self.canvas.figure.tight_layout()
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.05, y=0.1)

        # Cores condicionais
        colors = []
        for valor in y:
            if valor == max_y:
                colors.append("tomato")       # vermelho para o maior valor
            elif valor == min_y:
                colors.append("limegreen")    # verde para o menor valor
            else:
                colors.append("skyblue")      # padrão

        # Plota o histograma com cores personalizadas
        self.canvas.axes.bar(labels, y, color=colors, edgecolor='black')

        # Linha do fator de carga
        self.canvas.axes.axhline(y=fator, color='red', linestyle='--', label="fator de carga")

        # Legenda
        self.canvas.axes.legend(loc='upper left')

        # Renderiza
        self.canvas.draw()

        # Botão para voltar pro menu principal
        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(200, 40)
        button_back.clicked.connect(self.showMainMenu)

        # Adiciona os botões e o gráfico no layout do widget
        layout.addWidget(label_select, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.canvas)
        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(20, 0, 20, 40)

        widget.setLayout(layout)
        self.setCentralWidget(widget)  # Renderiza na tela o widget criado

    # Terceira Metodologia
    def showHashPrimo(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        # Widget e layout principal
        widget = QWidget()
        layout = QVBoxLayout()

        # Título
        label_select = QLabel("Metodologia 4")
        label_select.setFont(FONT)

        # Label e caixa de seleção (QComboBox)
        label_m = QLabel("Selecione o valor de M:")
        label_m.setFont(QFont("Arial", 18))

        self.combo_m = QComboBox()
        self.combo_m.setFont(QFont("Arial", 18))
        self.combo_m.addItems(["17", "43", "97"])
        self.combo_m.setFixedWidth(150)

        # Layout horizontal para o seletor de M
        input_layout = QHBoxLayout()
        input_layout.addWidget(label_m)
        input_layout.addWidget(self.combo_m)
        input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        # Botão para gerar o gráfico
        button_generate = QPushButton("Gerar Gráfico")
        button_generate.setFont(FONT)
        button_generate.setFixedSize(250, 50)
        button_generate.clicked.connect(self.gerarGrafico)

        # Botão para voltar ao menu principal
        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(200, 40)
        button_back.clicked.connect(self.showMainMenu)

        # Monta o layout principal
        layout.addWidget(label_select, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(input_layout)
        layout.addWidget(self.canvas)
        layout.addWidget(button_generate, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(20, 0, 20, 40)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
             
    def showHashPares(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        # Widget e layout principal
        widget = QWidget()
        layout = QVBoxLayout()

        # Título
        label_select = QLabel("Metodologia 4")
        label_select.setFont(FONT)

        # Label e caixa de seleção (QComboBox)
        label_m = QLabel("Selecione o valor de M:")
        label_m.setFont(QFont("Arial", 18))

        self.combo_m = QComboBox()
        self.combo_m.setFont(QFont("Arial", 18))
        self.combo_m.addItems(["16", "40", "100"])
        self.combo_m.setFixedWidth(150)

        # Layout horizontal para o seletor de M
        input_layout = QHBoxLayout()
        input_layout.addWidget(label_m)
        input_layout.addWidget(self.combo_m)
        input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        # Botão para gerar o gráfico
        button_generate = QPushButton("Gerar Gráfico")
        button_generate.setFont(FONT)
        button_generate.setFixedSize(250, 50)
        button_generate.clicked.connect(self.gerarGrafico)

        # Botão para voltar ao menu principal
        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(200, 40)
        button_back.clicked.connect(self.showMainMenu)

        # Monta o layout principal
        layout.addWidget(label_select, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(input_layout)
        layout.addWidget(self.canvas)
        layout.addWidget(button_generate, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(20, 0, 20, 40)

        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def gerarGrafico(self):
        """Gera o gráfico de colisões com base no valor de M selecionado"""
        M = int(self.combo_m.currentText())

        # Pega os dados 
        x, y, fator = resultPrimo(M)

        # Limpa o gráfico anterior
        self.canvas.axes.clear()

        # Encontra o maior e o menor número de colisões
        max_y = max(y)
        min_y = min(y)

        # Configuração do gráfico
        self.canvas.axes.set_title(f"M = {M}", fontsize=16)
        self.canvas.axes.set_xlabel("Posição do hash")
        self.canvas.axes.set_ylabel("Quantidade de colisões")
        self.canvas.figure.tight_layout()
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.02, y=0.1)

        # Cores condicionais (mesmo estilo da Metodologia 1)
        colors = []
        for valor in y:
            if valor == max_y:
                colors.append("tomato")       # vermelho = maior colisão
            elif valor == min_y:
                colors.append("limegreen")    # verde = menor colisão
            else:
                colors.append("skyblue")      # padrão

        # Plota o histograma
        self.canvas.axes.bar(
            x,
            y,
            color=colors,
            edgecolor="black",
            linewidth=0.6,
            alpha=0.9,
            width=0.8
        )

        # Linha do fator de carga
        self.canvas.axes.axhline(y=fator, color='red', linestyle='--', label="fator de carga")

        # 🔹 Mostra apenas alguns rótulos no eixo X (por exemplo, a cada 10 posições)
        step = max(1, len(x) // 10)  # mostra cerca de 10 rótulos
        ticks = list(range(0, len(x), step))
        self.canvas.axes.set_xticks(ticks)
        self.canvas.axes.set_xticklabels(ticks, rotation=0, fontsize=8) # type: ignore

        # Legenda
        self.canvas.axes.legend(loc='upper left')

        # Renderiza o gráfico
        self.canvas.draw()



    # Sai da aplicacao
    def exitAplication(self):
        sys.exit()
    