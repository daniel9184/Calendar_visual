from PyQt6.QtGui import QColor, QTextCharFormat
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QWidget
from datetime import date
from ui_calendar import Ui_Form
from functions_and_dict import conversor, get_days_of_month
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


class My_widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setWindowIcon(QIcon('icons/calendar.svg'))
        self.current_date = self.calendarWidget.selectedDate().toPyDate()
        self.current_day_of_scale = None
        self.pushButton.clicked.connect(self.hide)
        # self.pushButton.setIcon(QIcon('icons/esq.ico'))

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
        date_selected = self.calendarWidget.selectedDate().toPyDate()
        result = self.is_dayoff(date_selected)
        # strftime transforma data selecionada em texto, e monta a frase de saída utilizando os termos do dicionário
        # conversor, que transforma o resultado (número de 0 a 8) em um dia da escala.
        date_plain_text = date_selected.strftime(f'O dia %d de %B de %Y é o seu {conversor[result]} na escala.')
        self.label_3.setText(date_plain_text)

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
