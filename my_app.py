from instr import *

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()# устанавливает, как будет выглядеть окно
    self.initUI() # создаём и настраиваем графические элементы
    self.connects() # устанавливает связи между элементами
    self.show() # старт

    def set_appear(self): 
        pass
    def initUI(self): 
        pass
    def connects(self): 
        pass
    def show(self): 
        pass
 def set_appear(self): 
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)


def initUI(self):
    self.hello_text = QLabel( txt_hello )
    self.instruction = QLabel( txt_instruction )
    self.button = QPushButton( txt_next )
    self.layout = QVBoxLayout()
    self.hello_text.addWidget(self.layout)
    self.instruction.addWidget(self.layout)
    self.button.addWidget(self.layout)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit
)
