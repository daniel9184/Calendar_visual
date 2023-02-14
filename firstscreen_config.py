from widget import My_widget
from ui_main_screen import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow


class botoes_tela(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calendar = My_widget()
        self.pushButton_1.clicked.connect(self.button1)
        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.button3)
        self.pushButton_4.clicked.connect(self.button4)
        self.pushButton_5.clicked.connect(self.button5)
        self.pushButton_6.clicked.connect(self.button6)
        self.pushButton_7.clicked.connect(self.button7)
        self.pushButton_8.clicked.connect(self.button8)
        self.pushButton_9.clicked.connect(self.button9)

    def paint_the_calendar(self, scale):
        # self.hide()
        self.calendar = My_widget()
        self.calendar.current_day_of_scale = scale
        self.calendar.paint_the_days()
        self.calendar.show()
        self.calendar.calendarWidget.currentPageChanged.connect(self.calendar.paint_the_days)
        self.calendar.calendarWidget.selectionChanged.connect(self.calendar.check_selected_date)

    def button1(self):
        self.paint_the_calendar(0)

    def button2(self):
        self.paint_the_calendar(1)

    def button3(self):
        self.paint_the_calendar(2)

    def button4(self):
        self.paint_the_calendar(3)

    def button5(self):
        self.paint_the_calendar(4)

    def button6(self):
        self.paint_the_calendar(5)

    def button7(self):
        self.paint_the_calendar(6)

    def button8(self):
        self.paint_the_calendar(7)

    def button9(self):
        self.paint_the_calendar(8)
