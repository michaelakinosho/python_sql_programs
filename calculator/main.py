import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QGridLayout, QAction, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from PySide2.QtCharts import QtCharts

class MainWindow(QMainWindow):
	def __init__(self, widget):
		QMainWindow.__init__(self)
		self.setWindowTitle("Michael Akinosho's Calculator")

		#Menu
		self.menu = self.menuBar()
		self.home_menu = self.menu.addMenu("Home")

		std_calc_action = QAction("Standard", self)
		#std_calc_action.triggered.connect(self.std_calc)

		sci_calc_action = QAction("Scientific", self)
		#sci_calc_action.triggered.connect(self.sci_calc)

		exit_action = QAction("Exit", self)
		exit_action.setShortcut("Ctrl+Q")
		exit_action.triggered.connect(self.exit_app)

		self.home_menu.addAction(std_calc_action)
		self.home_menu.addAction(sci_calc_action)
		self.home_menu.addAction(exit_action)
		self.setCentralWidget(widget)

		#Status bar
		self.status = self.statusBar()
		self.status.showMessage("Calculator opened")

	@Slot()
	def exit_app(self, checked):
		QApplication.quit()

class Widget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		
		#for i in range(10):
			#self.(i) = Button(i)



		#Number 10 Keypad
		self.bZero = Button("0")
		self.bOne = QPushButton("1")
		self.bTwo = QPushButton("2")
		self.bThree = QPushButton("3")
		self.bFour = QPushButton("4")
		self.bFive = QPushButton("5")
		self.bSix = QPushButton("6")
		self.bSeven = QPushButton("7")
		self.bEight = QPushButton("8")
		self.bNine = QPushButton("9")

		self.TenKeyPad = QGridLayout()
		x = 0
		y = 0
		for b in range(10):
			bt = 9-b
			button = QPushButton('%d' %bt)
			self.TenKeyPad.addWidget(button, 0, b)


		self.layout = QHBoxLayout()

		self.layout.addLayout(self.TenKeyPad)

		self.setLayout(self.layout)

class Button(QPushButton):
	def __init__(self, s):
		QPushButton.__init__(self)

if __name__=="__main__":
	#Qt Application
	app = QApplication(sys.argv)
	#QWidget
	widget = Widget()
	#QMainWindow using QWidget as central widget
	window = MainWindow(widget)

	window.resize(800,600)
	window.show()

	#Execute application
	sys.exit(app.exec_())