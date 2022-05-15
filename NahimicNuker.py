import sys
import psutil
import ctypes
import logging
from ui_main import *

class Application(Ui_MainWindow):
    def __init__(self,window):
        self.setupUi(window)
        self.GoButton.clicked.connect(self.GoClicked)
        self.MoboManufacturercomboBox.activated.connect(self.onMoboBoxChanged)
    
    def GoClicked(self):
        print(self.MoboManufacturercomboBox.currentText())
        print(self.BlacklistIDsCheckbox.isChecked())
    
    def onMoboBoxChanged(self):
        self.GoButton.setEnabled(True)
        self.MoboManufacturercomboBox.model().item(0).setEnabled(False)

if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.user32.MessageBoxW(0, "This software needs to be run as administrator", "Oh no", 0)
        sys.exit()
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Application(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())

def nuke():
    isrunning = "NahimicService.exe" in (p.name() for p in psutil.process_iter())
    
