import sys
import psutil
import ctypes
import os
import logging
import win32api
import win32serviceutil
from ui_main import *

def nuke():
        isrunning = "NahimicService.exe" in (p.name() for p in psutil.process_iter())
        if isrunning:
            logging.info("NahimicService is running")
        sys32exeinstalled = os.path.exists("C:\Windows\System32\\NahimicService.exe")
        if sys32exeinstalled:
            logging.info("Found NahimicService.exe in System32")
        
        try:
            serviceisrunning = True if win32serviceutil.QueryServiceStatus("NahimicService")[1] == 4 else False
            print(serviceisrunning)
        except Exception as ex:
            logging.debug(ex)
            servicefound = False
        else:
            logging.info("Found the NahimicService Service")
            servicefound = True


class Application(Ui_MainWindow):
    def __init__(self,window):
        self.setupUi(window)
        self.GoButton.clicked.connect(self.GoClicked)
        self.MoboManufacturercomboBox.activated.connect(self.onMoboBoxChanged)
    
    def GoClicked(self):
        print(self.MoboManufacturercomboBox.currentText())
        print(self.BlacklistIDsCheckbox.isChecked())
        nuke()
    
    def onMoboBoxChanged(self):
        self.GoButton.setEnabled(True)
        self.MoboManufacturercomboBox.model().item(0).setEnabled(False)

if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.user32.MessageBoxW(0, "This software needs to be run as administrator", "Oh no", 0)
        sys.exit()
    
    logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Application(MainWindow)

    MainWindow.show()

    sys.exit(app.exec())


