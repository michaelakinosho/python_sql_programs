from os.path import expanduser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

home_directory = expanduser("~")

class DirModel(QDirModel):
    def data(self, index, role):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignVCenter
        return super(DirModel, self).data(index, role)

app = QApplication([])
model = DirModel()
view = QTableView()
view.setModel(model)
view.setRootIndex(model.index(home_directory))
view.show()
app.exec()
