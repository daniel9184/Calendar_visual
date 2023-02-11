from tkinter import *
import tkinter.scrolledtext as st
import locale, calendar
from datetime import date, timedelta

class Tela():
    def __init__(self):
        root = Tk()
        self.root = root
        self.Tela_entrada()
        self.valorA = IntVar()
        self.Frames_tela()
        self.Raiz()
        root.mainloop()

    def Tela_entrada(self):
        self.root.title('Calendário')
        # self.root.iconbitmap('diamond.ico')
        self.root.geometry('1060x635+30+1')
        self.root.resizable(True,True)
        self.root.configure(background='LightCyan')

    def Frames_tela(self):
        import tkinter.font as tkFont
        self.frame1 = Frame(self.root, bd=3, bg='LightBlue', highlightthickness=2, highlightcolor='LightSteelBlue')
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.09)
        self.Lb_dia = Label(self.frame1 , text= 'Hoje é...',background ='LightCyan')
        self.Lb_dia.place(relx=0.45, rely=0.1, relwidth=0.15, relheight=0.35)
        self.ra_1 = Radiobutton(self.frame1, text='1º Dia Escala', variable=self.valorA , value=1 ,bg='LightBlue',
                                command= self.Raiz )
        self.ra_2 = Radiobutton(self.frame1, text='2º Dia Escala', variable=self.valorA , value=2 ,bg='LightBlue',
                                command= self.Raiz )
        self.ra_3 = Radiobutton(self.frame1, text='3º Dia Escala', variable=self.valorA , value=3 ,bg='LightBlue',
                                command=self.Raiz)
        self.ra_4 = Radiobutton(self.frame1, text='4º Dia Escala', variable=self.valorA , value=4 ,bg='LightBlue',
                                command=self.Raiz)
        self.ra_5 = Radiobutton(self.frame1, text='5º Dia Escala', variable=self.valorA , value=5 ,bg='LightBlue',
                                command=self.Raiz)
        self.ra_6 = Radiobutton(self.frame1, text='6º Dia Escala', variable=self.valorA , value=6 ,bg='LightBlue',
                                command=self.Raiz)
        self.ra_7 = Radiobutton(self.frame1, text='1º Dia FOLGA', variable=self.valorA , value=7 ,bg='LightBlue',
                                command=self.Raiz)
        self.ra_8 = Radiobutton(self.frame1, text='2º Dia FOLGA', variable=self.valorA , value=8 ,bg='LightBlue',
                                command=self.Raiz)
        self.ra_9 = Radiobutton(self.frame1, text='3º Dia FOLGA', variable=self.valorA, value=9, bg='LightBlue',
                                command=self.Raiz)
        self.ra_1.place(relx=0.01, rely=0.6,relwidth=0.09,relheight=0.3)
        self.ra_2.place(relx=0.11, rely=0.6, relwidth=0.09, relheight=0.3)
        self.ra_3.place(relx=0.22, rely=0.6, relwidth=0.09, relheight=0.3)
        self.ra_4.place(relx=0.33, rely=0.6, relwidth=0.09, relheight=0.3)
        self.ra_5.place(relx=0.44, rely=0.6, relwidth=0.09,relheight=0.3)
        self.ra_6.place(relx=0.55, rely=0.6, relwidth=0.09, relheight=0.3)
        self.ra_7.place(relx=0.68, rely=0.6, relwidth=0.1, relheight=0.3)
        self.ra_8.place(relx=0.79, rely=0.6, relwidth=0.1, relheight=0.3)
        self.ra_9.place(relx=0.9, rely=0.6, relwidth=0.1, relheight=0.3)
        self.valorA.set(7)
        self.frame2 = Frame(self.root, bd=3,bg='LightBlue' , highlightthickness=2 , highlightcolor='LightSteelBlue')
        self.frame2.place(relx=0.01 , rely=0.11 , relwidth=0.98 , relheight=0.87)
        self.Cx_texto = st.ScrolledText(self.frame2, font='Courier 10')
        self.Cx_texto.place(relx=0.01 , rely=0.01 , relwidth=0.98 , relheight=0.98 )
        self.Cx_texto.tag_config('found', foreground= 'red', font='Courier 10 bold')
        # como descobrir a fonte !!! + o importe do tkFont
        # font = tkFont.Font(font=self.Cx_texto['font'])
        # print(font.actual())

    def Raiz(self):
        locale.setlocale(locale.LC_ALL, 'pt')
        self.ano_atual = date.today().year
        self.mes_atual = date.today().month
        self.dia_atual = self.Dia_escala()
        self.dia_atual = self.dia_atual.day
        self.calendario1 = self.cria_calendario(self.ano_atual)
        self.calendario2 = self.cria_calendario(self.ano_atual + 1)
        self.escala = self.calendario1 + self.calendario2
        self.escala_pronta = self.comeca_F(self.escala)
        self.meses_escala = self.separa_mes()
        # print(self.meses_escala[0]);input()
        self.apresenta = self.separa_linhas()
        self.texto_Apresenta()

    def cria_calendario(self,anoRef):
        if anoRef == self.ano_atual:
            if self.mes_atual > 0 and self.mes_atual < 5: meses = 1
            if self.mes_atual > 4 and self.mes_atual < 9: meses = 5
            if self.mes_atual > 8 and self.mes_atual < 13: meses = 9
        else:
            meses = 1
        calendar.setfirstweekday(6)
        anot = ''
        for corre in range(meses, 13):
            passoIt = calendar.month(anoRef, corre, 3)
            passoIt = '  ' + passoIt.replace(str(anoRef), '')  # retirar o ano dos meses...
            anot += passoIt
        ano = anot
        return ano

    def comeca_F(self,escala):
        corre = len(escala) - 1
        inicio = calendar.month_name[self.mes_atual]
        if self.mes_atual==12 :
            final = calendar.month_name[1]
        else:
            final = calendar.month_name[(self.mes_atual + 1)]
        strInico = escala.find(inicio)
        strFinal = escala.find(final)
        busca = escala[strInico:strFinal]
        Mbusca = busca.find(str(self.dia_atual))
        troca1 = strInico + Mbusca
        contagem = 0
        for crd in range(troca1, corre):
            antes = escala[(crd - 1):crd];
            antes2 = escala[(crd - 2):(crd - 1)]
            eu = escala[crd:(crd + 1)]
            depois = escala[(crd + 1):(crd + 2)]
            if eu.isnumeric() and (antes.isnumeric() or antes.isspace()) and (
                    depois.isspace() or depois == '\n') and antes2.isspace():
                contagem += 1
                if contagem < 4 and contagem > 0:
                    if antes.isnumeric():
                        esc1 = escala[:(crd - 1)] + 'F '
                        esc2 = escala[(crd + 1):]
                        Nesc = esc1 + esc2
                        escala = Nesc
                    else:
                        esc1 = escala[:(crd - 1)] + 'F '
                        esc2 = escala[(crd + 1):]
                        Nesc = esc1 + esc2
                        escala = Nesc
                if contagem > 8:
                    contagem = 0
        return escala

    def Dia_escala(self):
        minha_data = date.today()
        perguntaescala = self.valorA.get()

        if perguntaescala == 1:
            minha_data = date.today() + timedelta(6)
        elif perguntaescala == 2:
            minha_data = date.today() + timedelta(5)
        elif perguntaescala == 3:
            minha_data = date.today() + timedelta(4)
        elif perguntaescala == 4:
            minha_data = date.today() + timedelta(3)
        elif perguntaescala == 5:
            minha_data = date.today() + timedelta(2)
        elif perguntaescala == 6:
            minha_data = date.today() + timedelta(1)
        elif perguntaescala == 7:
            minha_data = date.today()
        elif perguntaescala == 8:
            minha_data = date.today() - timedelta(1)
        elif perguntaescala == 9:
            minha_data = date.today() - timedelta(2)
        else:
            minha_data = date.today() - timedelta(2)
        return minha_data

    def separa_mes(self):
        contagem = len(self.escala_pronta)
        # print(self.escala_pronta);input()
        l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = meu_mes = pega_mes = T_meu_mes = ''
        meses = linhas = fatia = inicio_mes = inicio_inicio = t_meses = fatia2 = 0
        ano_div = []
        # ************************************** Aqui só pra saber quantos meses tem a escala...
        for corre2 in range(0, contagem):
            if self.escala_pronta[corre2] == '\n':
                T_meu_mes = self.escala_pronta[fatia2:corre2]
                inicio_inicio = len(T_meu_mes)
                if T_meu_mes[0:5].isspace() and inicio_inicio < 27:
                    t_meses += 1
                fatia2 = corre2
        # ***************************** Agora sim a função em questão...
        for corre in range(0, contagem):
            if self.escala_pronta[corre] == '\n':
                meu_mes = self.escala_pronta[fatia:corre]
                inicio_inicio = len(meu_mes)
                if meu_mes[0:5].isspace() and inicio_inicio < 27:
                    meses += 1
                    if meses >= 1:
                        pega_mes = self.escala_pronta[(inicio_mes - inicio_inicio+1 ):(corre - inicio_inicio)]
                        if pega_mes != '':
                            if pega_mes[0] == '\n':
                                pega_mes = self.escala_pronta[(inicio_mes - inicio_inicio + 2):(corre - inicio_inicio)]
                            if pega_mes[0:2] == ' \n':
                                self.pega_mes = self.escala_pronta[(inicio_mes - inicio_inicio + 3):(corre - inicio_inicio)]
                            if pega_mes[-1] != '\n':
                                pega_mes += '\n'
                        ano_div.append(pega_mes)
                    inicio_mes = corre
                    if meses == t_meses:
                        pega_mes = self.escala_pronta[(inicio_mes - inicio_inicio + 1):]
                        if pega_mes[0] == '\n':
                            pega_mes = self.escala_pronta[(inicio_mes - inicio_inicio + 2):]
                        if pega_mes[0:2] == ' \n':
                            pega_mes = self.escala_pronta[(inicio_mes - inicio_inicio + 3):]
                        if pega_mes[-1] != '\n':
                            pega_mes += '\n'
                        ano_div.append(pega_mes)
                fatia = corre
        return ano_div

    def separa_linhas(self):
        qtd_meses = len(self.meses_escala)
        Apresenta=''
        for corre_escala in range(0, qtd_meses, 4):
            ctg_linha = ctg_bloco = meu_mes_T = 0
            l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = olha_linha = ''
            for ciclo in range(4):
                meu_mes = self.meses_escala[ciclo + corre_escala]
                fatia = ctg_linha = 0
                l11 = l22 = l33 = l44 = l55 = l66 = l77 = l88 = ''
                for M_linhas in range(len(meu_mes)):
                    if meu_mes[M_linhas] == '\n':
                        ctg_linha += 1
                        olha_linha = meu_mes[fatia:M_linhas]
                        if len(olha_linha) < 27:
                            olha_linha = olha_linha + (' ' * (28 - len(olha_linha)))
                        olha_linha = olha_linha.replace('\n', '')

                        if ctg_linha == 1:
                            l11 = olha_linha
                        elif ctg_linha == 2:
                            l22 = olha_linha
                        elif ctg_linha == 3:
                            l33 = olha_linha
                        elif ctg_linha == 4:
                            l44 = olha_linha
                        elif ctg_linha == 5:
                            l55 = olha_linha
                        elif ctg_linha == 6:
                            l66 = olha_linha
                        elif ctg_linha == 7:
                            l77 = olha_linha
                        elif ctg_linha == 8:
                            l88 = olha_linha
                        fatia = M_linhas
                if l66 == '': l66 = ' ' * 27
                if l77 == '': l77 = ' ' * 27
                if l88 == '': l88 = ' ' * 27

                # print(ciclo)
                l1 = l1 + l11 + '   '
                l2 = l2 + l22 + '   '
                l3 = l3 + l33 + '   '
                l4 = l4 + l44 + '   '
                l5 = l5 + l55 + '   '
                l6 = l6 + l66 + '   '
                l7 = l7 + l77 + '   '
                l8 = l8 + l88 + '   '
            Apresenta = Apresenta+ (l1 + '\n' + l2 + '\n' + l3 + '\n' + l4 + '\n' + l5 + '\n' + l6 + '\n' + l7 + '\n' + l8 + '\n')

        return Apresenta

    def texto_Apresenta(self):
        self.Cx_texto.delete("0.0","end")
        self.Cx_texto.insert("end", self.apresenta)
        i_tag='1.0'
        while True:
            pos = self.Cx_texto.search(pattern=' F ', index=i_tag, stopindex='end', count=True)
            if not pos:
                break
            else:
                self.Cx_texto.tag_add('found', pos, (pos + '+3c'))
                i_tag = pos + '+1c'
        self.Cx_texto.focus

Tela()