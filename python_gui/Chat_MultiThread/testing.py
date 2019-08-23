
from threading import *
from PyQt5.QtWidgets import QApplication
from threadutil import CurrentThread

print_thread = lambda: print(current_thread().name)
print_thread()
Thread(target=print_thread).start()

app = QApplication([])
main_thr = CurrentThread()
Thread(target=lambda: main_thr.execute(print_thread)).start()
app.exec()
