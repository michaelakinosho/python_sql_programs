import sys
import pandas as pd
from decimal import *
from PySide2.QtCore import Qt, Slot, QObject
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QGridLayout, QAction, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QButtonGroup, QAbstractButton, QStackedWidget, QStackedLayout, QSizePolicy)
from PySide2.QtCharts import QtCharts

df = pd
class MainWindow(QMainWindow):
	def __init__(self, widget):
		QMainWindow.__init__(self)
		self.setWindowTitle("Michael Akinosho's Calculator")

		#Menu
		self.menu = self.menuBar()
		self.home_menu = self.menu.addMenu("Home")

		std_calc_action = QAction("Standard", self)

		sci_calc_action = QAction("Scientific", self)

		exit_action = QAction("Exit", self)
		exit_action.setShortcut("Ctrl+Q")
		exit_action.triggered.connect(self.exit_app)
		std_calc_action.triggered.connect(lambda: widget.stack_widget.setCurrentIndex(0))
		sci_calc_action.triggered.connect(lambda: widget.stack_widget.setCurrentIndex(1))

		self.home_menu.addAction(std_calc_action)
		self.home_menu.addAction(sci_calc_action)
		self.home_menu.addAction(exit_action)
		self.setCentralWidget(widget)

		#Status bar
		self.status = self.statusBar()
		self.status.showMessage("Calculator opened")
		#print(widget.stack_widget.currentIndex())
		#widget.stack_widget.setCurrentIndex(0)

	@Slot()
	def exit_app(self, checked):
		QApplication.quit()

class MainWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		global df
		df = CalcFunctions()

		self.stack_widget = QStackedLayout()

		self.std_display = DisplayWidget()
		self.sci_display = DisplayWidget()
		self.std_calc_widget = StdCalcWidget()
		self.sci_calc_widget = SciCalcWidget()

		self.std_calc_widget.std_layout.insertWidget(0,self.std_display)
		self.sci_calc_widget.sci_vert_layout.insertWidget(0,self.sci_display)

		self.std_calc_widget.TenKeyPad.buttonClicked[QAbstractButton].connect(self.doCalc)
		self.sci_calc_widget.std1.TenKeyPad.buttonClicked[QAbstractButton].connect(self.doCalc)

		self.layout = QVBoxLayout()
		
		#self.setLayout(self.layout)
		self.stack_widget.addWidget(self.std_calc_widget)
		self.stack_widget.addWidget(self.sci_calc_widget)
		self.setLayout(self.stack_widget)

	def doCalc(self, button):
		displayText = self.std_display.display.text()
		
		buttonText = button.text()
		print("Text is: {} and type of text: {}".format(self.std_display.display.text(), type(self.std_display.display.text())))
		print("Display Text is: {} and type of text: {}".format(displayText, type(displayText)))
		print("Button Text is: {} and type of text: {}".format(button.text(), type(button.text())))
		try:
			if buttonText in ["0","1","2","3","4","5","6","7","8","9","."]:
				if displayText == "0":
					if buttonText == ".":
						buttonText = ("0"+buttonText)
					self.std_display.display.clear()
					self.std_display.display.setText(buttonText)
					self.sci_display.display.setText(self.std_display.display.text())
				elif displayText != "0":
					if buttonText == "." and buttonText in displayText:
						pass
					else:
						self.std_display.display.setText(displayText + buttonText)
						self.sci_display.display.setText(self.std_display.display.text())

			else:
				color = button.palette().button().color()
				print("Button color name before change is: {} and color code is {}".format(color.name(), color))
				button.setStyleSheet('QPushButton {background-color: #a3c1da;}')
				print("testing")
				print(button.text())
		except ValueError:
			displayText = displayText
		except:
			displayText = displayText

class DisplayWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		#initialize the display area
		self.dsp_layout = QVBoxLayout()

		self.display = QLineEdit()
		self.display.setText("0")
		self.display.setAlignment(Qt.AlignRight)
		self.display.setReadOnly(True)

		self.setLayout(self.dsp_layout)

		self.dsp_layout.addWidget(self.display)

class StdCalcWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		#df.prnFun()

		#initialize the ten key pad
		self.tenkeyLayout = QGridLayout()
		self.TenKeyPad = QButtonGroup()

		std_b_list = ["MC","MR","MS","M+","M-","<--","CE","C","+ -","SQRT","7","8","9","/","%","4","5","6","*","1" + "/" + "x","1","2","3","-","=","0"," ",".","+"," "]
		x = 0
		y = 0
		for i in std_b_list:
			button = QPushButton(i)

			button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

			if button.text() != " ":
				if button.text() == "0":
					self.tenkeyLayout.addWidget(button, x, y,1,2)
				elif button.text() == "=":
					self.tenkeyLayout.addWidget(button, x, y,2,1)
				else:
					self.tenkeyLayout.addWidget(button, x, y,1,1)
				self.TenKeyPad.addButton(button)
			y += 1
			if y == 5:
				x += 1
				y = 0
		
		self.std_disp = DisplayWidget()

		self.std_layout = QVBoxLayout()

		self.std_layout.addLayout(self.tenkeyLayout)

		self.setLayout(self.std_layout)

class SciCalcWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.std1 = StdCalcWidget()

		#initialize the scientific key pad
		self.scikeyLayout = QGridLayout()
		self.SciKeyPad = QButtonGroup()

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

		self.sci_layout = QHBoxLayout()
		self.sci_layout.addLayout(self.scikeyLayout)
		self.sci_layout.addWidget(self.std1)

		self.sci_vert_layout = QVBoxLayout()
		self.sci_vert_layout.addLayout(self.sci_layout)

		self.setLayout(self.sci_vert_layout)

class CalcFunctions():
	def __init__(self):
		self.dfc = pd
		self.load_funcs()

	def __str__(self):
		print(str(self.dfc.name))

	def prnFun(self):
		print(self.dfc)

	def load_funcs(self):
		try:
			self.dfc = pd.read_csv("functions_file.csv")
		except IOError:
			print("Unable to load functions file")
		except:
			print("Unable to load functions file")

if __name__=="__main__":
	#Qt Application
	app = QApplication(sys.argv)
	#QWidget
	widget = MainWidget()
	#QMainWindow using QWidget as central widget
	window = MainWindow(widget)

	window.resize(10,10)
	window.show()

	#Execute application
	sys.exit(app.exec_())