from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import sys

appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

def show_about_dialog():
    text = "<center>" \ 						#start of tag to center image
       "<h1>Text Editor</h1>" \
       "<img src=%r>" \							#link to image resource
       "</center>" \							#end of tag to center image
       "<p>Version 31.4.159.265358<br/>" \		#additional placeholder for about dialog
       "Copyright &copy; Company Inc.</p>" \	
       % appctxt.get_resource("icon.svg")
    about_dialog = QMessageBox(window)
    about_dialog.setText(text)
    about_dialog.exec_()
about_action.triggered.connect(show_about_dialog)

exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
sys.exit(exit_code)