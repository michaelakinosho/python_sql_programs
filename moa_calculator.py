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
		self.file_menu = self.menu.addMenu("File")

		std_calc_action = QAction("Standard", self)
		std_calc_action.triggered.connect(self.std_calc)

		sci_calc_action = QAction("Scientific", self)
		sci_calc_action.triggered.connect(self.sci_calc)

		self

	@Slot()
	def exit_app(self, checked):
		QApplication.quit()