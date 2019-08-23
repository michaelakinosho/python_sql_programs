import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

        #Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        self.label = QLineEdit()

        #Create layout and add QtWidgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        #Set dialog QVBoxLayout
        self.setLayout(layout)

        #Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)
        #self.label = self.edit.text()

    #Greets the user
    def greetings(self):
        self.label.setText(self.edit.text())
        print("Hello {}".format(self.edit.text()))
        #self.label = self.edit.text()

#if __name__=='__main__':
#Create the Qt application
app = QApplication(sys.argv)
#create and show the Form
form = Form()
form.show()
#Run the main Qt loop
sys.exit(app.exec_())
