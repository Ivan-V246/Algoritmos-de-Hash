from pathlib import Path
import json
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

    def getData(self, algorithm) -> dict:
        tam = [100, 250, 500]
        dados = {}
        for i in range(3):
            soma = 0
            pasta_atual = Path(__file__).parent.parent.parent  # src/
            arquivo_json = pasta_atual / "data_base" / algorithm / f"{algorithm}_{tam[i]}.json"
            
            with open(arquivo_json, "r", encoding="utf-8") as f:
                data = json.load(f)
            for j in range (len(data)):
                soma += data[j]["tempo"]
            dados[tam[i]] = (soma/len(data))
        return dados