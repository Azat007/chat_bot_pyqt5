import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel,QGridLayout,QMainWindow
from PyQt5.QtCore import QCoreApplication
import design


class Example(QMainWindow, design.Ui_Dialog):

    def __init__(self, key, **d ):
        super().__init__()


        self.key=key
        self.d=d
        self.setupUi(self)
        self.initUI( **d)



    def initUI(self, **d):
            self.btn=[]
            self.textBrowser.append('- '+d[self.key][0])
            i, j= 0, 0
            for k in range(1,len(d[self.key]),1):
                self.btn.append(QPushButton(d[self.key][k]))
                self.gridLayout.addWidget(self.btn[k-1], j, i)
                print(d[self.key][k])
                i+=1
                if i==3:
                    j+=1
                    i=0
            for i in range(len(self.btn)):
                self.btn[i].clicked.connect(self.prnt)
            self.show()
    def prnt(self):
        sending_button = self.sender()
        if str(sending_button.text())=='Bye':
            self.close()
        if str(sending_button.text())=='Вернуться в нало':
            self.key='Ok'
        else:
            self.key=(str(sending_button.text()))
        self.textBrowser.append('- '+str(sending_button.text()))
        while self.gridLayout.count():
            item = self.gridLayout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()

        self.initUI( **d)






if __name__ == '__main__':

    d={
        'start':['Привет', 'Привет','Bye'],
        'Привет':['Я робот, который поможет тебе выбрать, как отдохнуть', 'Ok','Bye'],
        'Ok': ['Вы хотите сходить куда-то бесплатно или готовы заплатить', 'Бесплатно', 'Готов заплатить', 'Bye'],
        'Бесплатно': ['Бесплатно можно сходить:', 'Галерея', 'Спорт', 'Bye'],
        'Спорт': ['Что вам нравится больше?', 'Футбол', 'баскетбол', 'фитнес'],
        'Футбол': ['В эти выходные состоятся матчи', 'Реал-Барса'],
        'Реал-Барса': ['Если это то, что вы хотели, нажмите Bye или вернитесь в начало ', 'Bye', 'Вернуться в нало'],
        'Готов заплатить': ['Замечательно, вам может будет интересно:', 'Кафе', 'Bye'],
        'Кафе': ['Если это то, что вы хотели, нажмите Bye или вернитесь в начало ', 'Bye', 'Вернуться в нало'] }

    key='start'

    app = QApplication(sys.argv)
    ex = Example(key,**d)
    sys.exit(app.exec_())