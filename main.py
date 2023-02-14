from PyQt6.QtWidgets import QApplication
from firstscreen_config import botoes_tela
import sys

app = QApplication(sys.argv)

windows1 = botoes_tela()
windows1.show()

app.exec()
