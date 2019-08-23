from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
app = QApplication([])

window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QTextEdit())
layout.addWidget(QLineEdit())
window.setLayout(layout)
window.show()
app.exec()
