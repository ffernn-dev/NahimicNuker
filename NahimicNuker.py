import sys
import psutil
import ctypes
import os
import logging
import win32api
import win32serviceutil
from ui_main import *

def nuke(motherboard, blacklistids):
        isrunning = "NahimicService.exe" in (p.name() for p in psutil.process_iter())
        if isrunning:
            logging.info("NahimicService is running")
        sys32exeinstalled = os.path.exists("C:\Windows\System32\\NahimicService.exe")
        if sys32exeinstalled:
            logging.info("Found NahimicService.exe in System32")
        
        driversfound = os.path.exists("C:\Windows\System32\DriverStore\FileRepository\\a-volutenh3aposwc.inf_amd64_1057edbba4c9a7b3") or os.path.exists("C:\Windows\System32\DriverStore\FileRepository\a-volutenh3aposwc.inf_amd64_d717bd2d70c0d848") or os.path.exists("C:\Windows\System32\DriverStore\FileRepository\avolutess3ext.inf_amd64_4262013e01267155") or os.path.exists("C:\Windows\System32\DriverStore\FileRepository\avolutess3vad.inf_amd64_79cd9525c9a5e12a") or os.path.exists("C:\Windows\System32\DriverStore\FileRepository\avolutess3vad.inf_amd64_b75dcc59f9f41ec0") or os.path.exists("C:\Windows\System32\DriverStore\FileRepository\avolutess3vad.inf_amd64_b75dcc59f9f41ec0")

        if motherboard == "MSI":
            foundindragoncenter = os.path.exists("C:\Program Files (x86)\MSI\One Dragon Center\\Nahimic")
        else:
            foundindragoncenter = False
        
        try:
            serviceisrunning = True if win32serviceutil.QueryServiceStatus("NahimicService")[1] == 4 else False
            print(serviceisrunning)
        except Exception as ex:
            logging.debug(ex)
            servicefound = False
        else:
            logging.info("Found the NahimicService Service")
            servicefound = True

        finaltext = ("\nStop the service and process" if serviceisrunning else "") + ("\nSet service startup type to disabled" if servicefound else "") + ("\nDelete the main exe" if sys32exeinstalled else "") + ("\nUninstall all related drivers" if driversfound else "") + ("\nDelete from MSI dragon center" if foundindragoncenter else "") + ("\nDelete various dlls" if False else "") + ("\nBlacklist driver IDs" if blacklistids else "") + ("\nDelete various (mostly empty for some reason) folders I found when searching")
        if ctypes.windll.user32.MessageBoxW(0, "The following actions will be taken to destroy Nahimic:\n" + finaltext + "\n\nContinue?", "Continue?", 4) == 6:
            
            if servicefound and serviceisrunning:
                win32serviceutil.StopService("NahimicService")
            if servicefound:
                os.system("sc config NahimicService start=disabled")

            if sys32exeinstalled:
                os.remove("C:\Windows\System32\\NahimicService.exe")
                os.remove("C:\Windows\System32\\NahimicSvc64.exe")

            if driversfound:
                os.system("pnputil /delete-driver avoluteess3.inf /force /uninstall")
                os.system("pnputil /delete-driver a-volutenh3aposwc.inf /force /uninstall")
                os.system("pnputil /delete-driver a-volutenh3aposwc.inf /force /uninstall")
                os.system("pnputil /delete-driver avolutess3vad.inf /force /uninstall")
                os.system("pnputil /delete-driver avolutess3vad.inf /force /uninstall")

            if foundindragoncenter:
                os.rmdir("C:\Program Files (x86)\MSI\One Dragon Center\\Nahimic")
            
            os.rmdir("C:\Windows\System32\A-Volute")
            os.remove("C:\Windows\System32\\NahimicAPO3ConfiguratorDaemonModule.dll")
            os.remove("C:\Windows\System32\\NahimicAPO4ConfiguratorDaemonModule.dll")
            os.remove("C:\Windows\System32\\NahimicPnPAPO4ConfiguratorDaemonModule.dll")
            os.remove("C:\Windows\System32\\NahimicService.ini")
            os.remove("C:\Windows\System32\\NahimicSvc64.exe")
            os.remove("C:\Windows\System32\\NAHIMICV3apo.dll")
            os.remove("C:\Windows\System32\\NAHIMICV3NSControl.dll")
            os.remove("C:\Windows\System32\\NAHIMICV3NSControlExpert.dll")
            os.remove("C:\Windows\SysWOW64\\NahimicSvc32.exe")

            localappdata = os.path.expandvars('%LOCALAPPDATA%')
            os.rmdir(localappdata + "\Packages\A-Volute.Nahimic_w2gh52qy24etm")
            os.rmdir(localappdata + "\\NhNotifSys")

            os.rmdir("C:\ProgramData\A-Volute")



class Application(Ui_MainWindow):
    def __init__(self,window):
        self.setupUi(window)
        self.GoButton.clicked.connect(self.GoClicked)
        self.MoboManufacturercomboBox.activated.connect(self.onMoboBoxChanged)
    
    def GoClicked(self):
        nuke(self.MoboManufacturercomboBox.currentText(), self.BlacklistIDsCheckbox.isChecked())
    
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


