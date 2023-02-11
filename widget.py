from PyQt6.QtGui import QColor
from PyQt6.QtGui import QTextCharFormat, QIcon
from PyQt6.QtCore import QDate
from ui_oficial import Ui_Form
from datetime import date
from PyQt6.QtWidgets import QWidget
from calendar_tests import conversor, get_days_of_month




class My_widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_date = self.calendarWidget.selectedDate().toPyDate()
        self.current_day_of_scale = None
        self.pushButton.clicked.connect(self.hide)
        self.pushButton.setIcon(QIcon('seta.ico'))

    def change_background(self, date_to_change):
        format_inst = QTextCharFormat()
        format_inst.setBackground(QColor(137, 153, 255))
        self.calendarWidget.setDateTextFormat(date_to_change, format_inst)

    def is_dayoff(self, other_date):
        data_atual = date.today()
        if other_date > data_atual:
            timedelta = (other_date - data_atual)
            result = timedelta.days + self.current_day_of_scale
        else:
            timedelta = (data_atual - other_date)
            result = timedelta.days * -1 + self.current_day_of_scale
        return result % 9

    def check_selected_date(self):
        try:
            date_selected = self.calendarWidget.selectedDate().toPyDate()
            result = self.is_dayoff(date_selected)
            self.label_3.setText(f'Esta data é seu {conversor[result]} na escala.')
            # print(f'Esta data é seu {conversor[result]} na escala.')
        except Exception as e:
            print("Erro:", type(e), e)

    def do_other(self):
        self.hide()

    def paint_the_days(self):
        try:
            current_year = self.calendarWidget.yearShown()
            current_month = self.calendarWidget.monthShown()
            visible_days = get_days_of_month(current_year, current_month)
            for day in visible_days:
                # checa se o resultado retornado por is_dayoff() resulta em folga ou não
                if self.is_dayoff(day) in [6, 7, 8]:
                    # converte em Qdate antes de mudar o background
                    self.change_background(QDate(day.year, day.month, day.day))
        except Exception as e:
            print("Erro:", type(e), e)
