import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QGridLayout, QAction, QApplicaiton, QHeaderView, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from PySide2.QtCharts import QtCharts

class MainWindow(QMainWindow):
	def __init__(self, widget):
		QMainWindow.__init__(self)
		self.setWindowTitle("Michael Akinosho's Calculator")

		#Menu
		self.menu = self.menuBar()
		self.home_menu = self.menu.addMenu("Home")

		std_calc_action = QAction("Standard", self)
		std_calc_action.triggered.connect(self.std_calc)

		sci_calc_action = QAction("Scientific", self)
		sci_calc_action.triggered.connect(self.sci_calc)

		exit_action = QAction("Exit", self)
		exit_action.setShortcut(QKeySequence.Quit)
		exit_action.triggered.connect(self.close)

		self.home_menu.addAction(std_calc_action)
		self.home_menu.addAction(sci_calc_action)
		self.home_menu.addAction(exit_action)

		#Status bar
		self.status = self.statusBar()
		self.status.showMessage("Calculator opened")

	@Slot()
	def exit_app(self, checked):
		QApplication.quit()

class Widget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.layout = QHBoxLayout()

		self.TenKeyPad = QGridLayout()
		self.SciKeyPad = QHBoxLayout()

		self.layout.addWidget(self.TenKeyPad)
		self.layout.addWidget(self.SciKeyPad)

		#Number 10 Keypad
		for i in 10:
			
		self.bZero = QPushButton("0")
		self.bOne = QPushButton("1")
		self.bTwo = QPushButton("2")
		self.bThree = QPushButton("3")
		self.bFour = QPushButton("4")
		self.bFive = QPushButton("5")
		self.bSix = QPushButton("6")
		self.bSeven = QPushButton("7")
		self.bEight = QPushButton("8")
		self.bNine = QPushButton("9")

if __name__!="__main__":
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