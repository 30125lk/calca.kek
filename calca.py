import sys 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from time import*
class UI(QWidget):
    def __init__(self):
        self.start()
        self.set()
    
    def start(self):
        self.ui = uic.loadUi('calca.ui')
        self.ui.show()

    def set(self):
        self.ui.button18.clicked.connect(lambda: self.click(num=0))
        self.ui.button5.clicked.connect(lambda: self.click(num=1))
        self.ui.button6.clicked.connect(lambda: self.click(num=2))
        self.ui.button7.clicked.connect(lambda: self.click(num=3))
        self.ui.button9.clicked.connect(lambda: self.click(num=4))
        self.ui.button10.clicked.connect(lambda: self.click(num=5))
        self.ui.button11.clicked.connect(lambda: self.click(num=6))
        self.ui.button13.clicked.connect(lambda: self.click(num=7))
        self.ui.button14.clicked.connect(lambda: self.click(num=8))
        self.ui.button15.clicked.connect(lambda: self.click(num=9))

        self.ui.button4.clicked.connect(lambda: self.click_equation('÷'))
        self.ui.button8.clicked.connect(lambda: self.click_equation('*'))
        self.ui.button12.clicked.connect(lambda: self.click_equation('-'))
        self.ui.button16.clicked.connect(lambda: self.click_equation('+'))

        self.ui.button20.clicked.connect(lambda: self.answer())
        self.ui.button1.clicked.connect(lambda: self.udalit())
        self.ui.button3.clicked.connect(lambda: self.back())
        self.ui.button2.clicked.connect(lambda: self.koren())             
    def click(self, num=0):
        self.display(text=num)

    def click_equation(self, num):
        global answer1
        self.display(num)
        answer1 = self.ui.label.text()
        self.ui.label.setText('0')

    def answer(self):
        answer2 = answer1 + self.ui.label.text()
        if '/0' in answer2:
            self.ui.label.setText('ERROR')
        else:
            answer2 = str(eval(answer2))
            self.ui.label.setText(answer2)



    def koren(self):
        x = self.ui.label.text()
        x = round(float(x)**0.5)
        self.ui.label.setText(str(x))

    def udalit(self):
        self.ui.label.setText(str(0))

    def back (self):
        x = self.ui.label.text()
        x = x[:-1]
        self.ui.label.setText(x)

    def display(self, text='0'):
        pld_text = self.ui.label.text()
        if pld_text == '0':
            pld_text = ''
        new_text = pld_text + str(text)
        self.ui. label.setText(new_text)
if __name__ == '__main__': 
    app = QApplication(sys.argv)
    uiWindow = UI()
    app.exec_()
