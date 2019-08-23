from PySide2.QtCore import QDateTime, Qt
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QHBoxLayout, QHeaderView, QSizePolicy, QTableView, QWidget)
from PySide2.QtCharts import QtCharts
from table_model import CustomTableModel

from datetime import datetime, timezone
import time

class Widget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)

        #Getting the Model
        self.model = CustomTableModel(data)

        #Creating a QTableView
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        #QTableView Headers
        self.horizontal_header = self.table_view.horizontalHeader()
        self.vertical_header = self.table_view.verticalHeader()
        self.horizontal_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.vertical_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.horizontal_header.setStretchLastSection(True)

        #Creating QtChart
        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.add_series("Magnitude(Column 1)", [0, 1])

        #Creating QChartView
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        #QWidget layout
        self.main_layout = QHBoxLayout()
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        ##Left layout
        size.setHorizontalStretch(1)
        self.table_view.setSizePolicy(size)
        self.main_layout.addWidget(self.table_view)

        ##Right Layout
        size.setHorizontalStretch(4)
        self.chart_view.setSizePolicy(size)
        self.main_layout.addWidget(self.chart_view)

        #Set the layout to the QWidget
        self.setLayout(self.main_layout)

    def add_series(self, name, columns):
        # Create QLineSeries
        self.series = QtCharts.QLineSeries()
        self.series.setName(name)

        # Filling QLineSeries
        for i in range(self.model.rowCount()):
            # Getting the data
            t = self.model.index(i, 0).data()
            date_fmt = "yyyy-MM-dd HH:mm:ss.zzz"

            x = float(QDateTime().fromString(t, date_fmt).toMSecsSinceEpoch())
            #print(type(x))
            y = float(self.model.index(i, 1).data())

            if x > 0 and y > 0:
                self.series.append(x, y)

        self.chart.addSeries(self.series)

        print(self.series.points()[0].x())
        #print(self.series.pointAdded(0))
        print(self.series.count())

        # Setting X-axis
        self.axis_x = QtCharts.QDateTimeAxis()

        self.axis_x.setTickCount(10)
        self.axis_x.setFormat("MM-dd (h:mm)")
        
        self.axis_x.setTitleText("Date")
        #print(self.axix_x.min())
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)

        self.series.attachAxis(self.axis_x)

        self.axis_x.setMin("2019-08-16 15:00:00.0600")
        self.axis_x.setMax("2019-08-17 18:00:00.000")

        #print(self.axis_x.min())

        # Setting Y-axis
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(20)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Magnitude")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

        self.series.attachAxis(self.axis_y)

        self.axis_y.setMin(-0.05)
        self.axis_y.setMax(5.5)

        # Getting the color from the QChart to use it on the QTableView
        self.model.color = "{}".format(self.series.pen().color().name())
