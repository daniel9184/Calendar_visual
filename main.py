from PyQt6.QtWidgets import QApplication
from buttons_configuration import botoes_tela
import sys

app = QApplication(sys.argv)

windows1 = botoes_tela()
windows1.show()

app.exec()
