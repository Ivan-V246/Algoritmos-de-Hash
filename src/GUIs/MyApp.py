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


        self.setWindowTitle("Algoritmos de Ordenação")
        self.setFixedSize(WINDOW_HEIGTH, WINDOW_WIDTH)
        self.setWindowIcon(QIcon(ICON2_PATH)) # Troca o icone da janela
        self.showMainMenu()  # Mostra a primeira janela


    # Renderiza o menu principal da aplicacao 
    def showMainMenu(self):
        CENTER = Qt.AlignmentFlag.AlignCenter # Cria um centralizacao 

        widget = QWidget() # Widget generico
        layout = QVBoxLayout() # Box vertical
        
        layout.setContentsMargins(0, 80, 0, 100) # Mergin no final e no inicio

        # Plota os gráficos usando os dados de ordenação
        button_view_graph = buttonMainMenu("Metodologia 1")
        button_view_graph.clicked.connect(self.metodologia1) # Adiciona funcao para esse botao
        
        # Compara Algoritmos
        button_compare_algorithms = buttonMainMenu("Metodologia 2")
        button_compare_algorithms.clicked.connect(self.metodologia2) # Adiciona funcao para esse botao
        
        button_metodologia3 = buttonMainMenu("Metodologia 3")
        button_metodologia3.clicked.connect(self.metodologia3) 
        
        # Sai da aplicacao
        button_report = buttonMainMenu("Sair")
        button_report.clicked.connect(self.exitAplication) # Adiciona funcao para esse botao

        # Adiciona os botoes no layout
        layout.addWidget(button_view_graph, alignment=CENTER)
        layout.addWidget(button_compare_algorithms, alignment=CENTER)
        layout.addWidget(button_metodologia3, alignment=CENTER)
        layout.addWidget(button_report, alignment=CENTER)
        
        widget.setLayout(layout) # Adiciona o layout no widget generico

        self.setCentralWidget(widget)  # Renderiza esse widget generico que foi criado 

    def metodologia1(self):
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
        print(fator)
    
        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.clear
        self.canvas.axes.set_title("Colisões do Hash", fontsize=16)
        self.canvas.axes.set_xlabel("Posição do Hash")
        self.canvas.axes.set_ylabel("Quantidade de colisões")
        self.canvas.figure.tight_layout()
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.05, y=0.1)
        self.canvas.axes.hist(x, bins=len(x), weights=y, color="skyblue", edgecolor='black')
        self.canvas.axes.plot([0,len(x)-1], [fator, fator], color='red', label="fator de carga")
        #self.canvas.axes.stem(fator, 70, orientation= "horizontal", linefmt='k:')
        self.canvas.axes.legend(loc='upper left')
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
        self.setCentralWidget(widget) # Renderiza na tela o widget criado

    def metodologia2(self):
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
        print(fator)
    
        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.clear
        self.canvas.axes.set_title("Colisões do Hash", fontsize=16)
        self.canvas.axes.set_xlabel("Posição do Hash")
        self.canvas.axes.set_ylabel("Quantidade de colisões")
        self.canvas.figure.tight_layout()
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.05, y=0.1)
        self.canvas.axes.hist(x, bins=len(x), weights=y, color="skyblue", edgecolor='black')
        self.canvas.axes.plot([0,len(x)-1], [fator, fator], color='red', label="fator de carga")
        #self.canvas.axes.stem(fator, 70, orientation= "horizontal", linefmt='k:')
        self.canvas.axes.legend(loc='upper left')
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
        self.setCentralWidget(widget) # Renderiza na tela o widget criado

    def metodologia3(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        # widget e layout da tela
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Seletor de Algoritmo para escolher quem vai ser usado
        label_select = QLabel("Metodologia 1")
        label_select.setFont(FONT)
        
        # Dados 
        x, y, fator = resultPrimo()
        print(fator)
        print(y)
    
        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.clear
        self.canvas.axes.set_title("Colisões do Hash", fontsize=16)
        self.canvas.axes.set_xlabel("Posição do Hash")
        self.canvas.axes.set_ylabel("Quantidade de colisões")
        self.canvas.figure.tight_layout()
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.05, y=0.1)
        self.canvas.axes.hist(x, bins=len(x), weights=y, color="skyblue", edgecolor='black')
        self.canvas.axes.plot([0,len(x)-1], [fator, fator], color='red', label="fator de carga")
        #self.canvas.axes.stem(fator, 70, orientation= "horizontal", linefmt='k:')
        self.canvas.axes.legend(loc='upper left')
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
        self.setCentralWidget(widget) # Renderiza na tela o widget criado

    # Sai da aplicacao
    def exitAplication(self):
        sys.exit()
    