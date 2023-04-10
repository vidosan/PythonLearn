import sys

from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QVBoxLayout, QComboBox, QDesktopWidget, QPushButton, \
    QHBoxLayout, QGridLayout, QLabel


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 spin box'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
            screen = QDesktopWidget().screenGeometry()
            width = screen.width()
            height = screen.height()
            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Добавление датчика')
            window = QWidget()
            self.layout =  QGridLayout(window)



            self.cb_name = QComboBox(self)
            self.cb_name.setToolTip("Имя")
            self.cb_name .addItems(['DA','DD','dP','DT','G'])
            self.cb_namenumber = QComboBox(self)
            for i in range(1, 101):
                self.cb_namenumber.addItem(str(i))

            self.cb_channel = QComboBox(self)
            for i in range(1, 101):
                self.cb_channel.addItem(str(i))

            self.cb_color= QComboBox(self)
            self.cb_color.addItems(['Cиний', 'Красный', 'Зелёный', 'Пурпурный'])

            self.cb_name_side= QComboBox(self)
            self.cb_name_side.addItems(['Лево', 'Право', 'Верх', 'Низ'])

            self.cb_reg = QComboBox(self)
            for i in range(1, 101):
                self.cb_reg .addItem(str(i))

            self.cb_X = QComboBox(self)

            for i in range(1, width):
                self.cb_X.addItem(str(i))
            self.cb_X.setCurrentIndex(int(width / 2))

            self.cb_Y = QComboBox(self)
            for i in range(1, height):
                self.cb_Y.addItem(str(i))
            self.cb_Y.setCurrentIndex(int(height / 2))

            self.confirm = QPushButton("Подтвердить", self)

            self.layout.addWidget(QLabel('Имя'),0,0)
            self.layouth1= QHBoxLayout()
            self.layouth1.addWidget(self.cb_name)
            self.layouth1.addWidget(self.cb_namenumber)
            self.layout.addLayout(self.layouth1, 0, 1)

            self.layout.addWidget(QLabel('Канал'), 1, 0)
            self.layout.addWidget( self.cb_channel, 1, 1)
            self.layout.addWidget(QLabel('Цвет'))
            self.layout.addWidget(self.cb_color)
            self.layout.addWidget(QLabel('Расположение имени'))
            self.layout.addWidget(self.cb_name_side)
            self.layout.addWidget(QLabel('Регистратор'))
            self.layout.addWidget(self.cb_reg)

            self.layout.addWidget(QLabel('X  Y'))

            self.layouth2 = QHBoxLayout()
            self.layouth2.addWidget(self.cb_X)
            self.layouth2.addWidget(self.cb_Y)
            self.layout.addLayout(self.layouth2, 5, 1)

            self.layout.addWidget(self.confirm, 6,0,2,0)
            self.setLayout( self.layout)
            self.confirm.clicked.connect(self.on_button_clicked)
            self.show()

    def on_button_clicked(self):

        clr = {'Красный': 're', 'Cиний': 'bl', 'Зелёный': 'gr', 'Пурпурный': 'pu'}.get(self.cb_color.currentText(), 'x')
        side = {'Лево': 'l', 'Право': 'r', 'Верх': 't', 'Низ': 'b'}.get(self.cb_name_side.currentText(), 'x')


        return ( f'{self.cb_name.currentText()+self.cb_namenumber.currentText()} {self.cb_channel.currentText()} {clr} {side} {self.cb_reg.currentText()} ({self.cb_X.currentText()} {self.cb_Y.currentText()})')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())