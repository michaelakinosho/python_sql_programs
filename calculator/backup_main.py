import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QGridLayout, QAction, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QButtonGroup, QAbstractButton, QStackedWidget, QStackedLayout)
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
		std_calc_action.triggered.connect(self.std_calc)
		sci_calc_action.triggered.connect(self.sci_calc)

		self.home_menu.addAction(std_calc_action)
		self.home_menu.addAction(sci_calc_action)
		self.home_menu.addAction(exit_action)
		self.setCentralWidget(widget)

		#Status bar
		self.status = self.statusBar()
		self.status.showMessage("Calculator opened")

	@Slot()
	def std_calc(self, widget):
		print("Standard Calculator")

	@Slot()
	def sci_calc(self, widget):
		print("Scientific Calculator")

	@Slot()
	def exit_app(self, checked):
		QApplication.quit()

class StdCalcWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		#initialize the ten key pad
		self.tenkeyLayout = QGridLayout()
		self.TenKeyPad = QButtonGroup()


class MainWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.scikeyLayout = QGridLayout()
		self.SciKeyPad = QButtonGroup()

		self.TenKeyPad.buttonClicked[QAbstractButton].connect(self.showNumber)
		
		std_b_list = ["MC","MR","MS","M+","M-","<--","CE","C","NEG","SQRT","7","8","9","/","%","4","5","6","*","1" + "/" + "x","1","2","3","-"," ","0"," ",".","+","="]
		x = 0
		y = 0
		for i in std_b_list:
			button = QPushButton(i)
			if button.text() != " ":
				self.tenkeyLayout.addWidget(button, x, y)
				self.TenKeyPad.addButton(button)
			y += 1
			if y == 5:
				x += 1
				y = 0

		sci_b_list = ["Deg","Rad","Grad"," "," "," ","Inv","ln","(",")","Int","sinh","sin","X²","n!","dms","cosh","cos","X^y","y√X","π","tanh","tan","X³","3√X","F-E","Exp","Mod","log","10^x"]
		x = 0
		y = 0
		for i in sci_b_list:
			button = QPushButton(i)
			if button.text() != " ":
				self.scikeyLayout.addWidget(button, x, y)
				self.SciKeyPad.addButton(button)

			y += 1
			if y == 5:
				x += 1
				y = 0

		self.display = QLineEdit()
		self.display.setText("0")
		self.display.setAlignment(Qt.AlignRight)
		self.display.setReadOnly(True)
		self.std_layout = QVBoxLayout()

		self.std_layout.addLayout(self.tenkeyLayout)

		self.sci_layout = QGridLayout()
		self.sci_layout.addLayout(self.scikeyLayout,0,0)
		self.sci_layout.addLayout(self.std_layout,0,1)
		
		self.stack_layout = QStackedLayout()

		self.stack_layout.addChildLayout(self.sci_layout)

		self.setLayout(self.stack_layout)

	def showNumber(self, button):
		try:
			intNum = int(self.display.text()+button.text())*2
		except ValueError:
			intNum = self.display.text()
		except:
			intNum = self.display.text()

		self.display.setText(str(intNum))

if __name__=="__main__":
	#Qt Application
	app = QApplication(sys.argv)
	#QWidget
	widget = MainWidget()
	#QMainWindow using QWidget as central widget
	window = MainWindow(widget)

	window.resize(600,600)
	window.show()

	#Execute application
	sys.exit(app.exec_())