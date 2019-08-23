import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile
from PySide2.QtCore import Slot

@Slot()
def greetings(myWin):
    print("Hello {}".format(myWin.lineEdit_2.text()))
    myWin.pushButton.clicked.connect(myWin.lineEdit_2.text())

if __name__=="__main__":
    app = QApplication(sys.argv)

    ui_file = QFile("mainwindow.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)

    #Add button signal to greetings slot
    window.pushButton.clicked.connect(window.lineEdit_2.setText(window.lineEdit.text()))
    ui_file.close()

    window.show()

    sys.exit(app.exec_())
