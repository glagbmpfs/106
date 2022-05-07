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
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit
)
