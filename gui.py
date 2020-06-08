#import PyQt5

import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Box Layout")
layout = QVBoxLayout()

layout.addWidget(QPushButton('left'))
layout.addWidget(QPushButton('center'))
layout.addWidget(QPushButton('right'))

window.setLayout(layout)

window.show()
sys.exit(app.exec_())



