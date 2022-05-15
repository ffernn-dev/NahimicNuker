# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(450, 540))
        MainWindow.setMaximumSize(QSize(450, 540))
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionCheck_out_my_website = QAction(MainWindow)
        self.actionCheck_out_my_website.setObjectName(u"actionCheck_out_my_website")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.GoButton = QPushButton(self.centralwidget)
        self.GoButton.setObjectName(u"GoButton")
        self.GoButton.setEnabled(False)
        self.GoButton.setGeometry(QRect(10, 130, 431, 81))
        font = QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.GoButton.setFont(font)
        self.ConfigBox = QGroupBox(self.centralwidget)
        self.ConfigBox.setObjectName(u"ConfigBox")
        self.ConfigBox.setGeometry(QRect(9, 10, 431, 107))
        font1 = QFont()
        font1.setBold(True)
        self.ConfigBox.setFont(font1)
        self.MoboManufacturercomboBox = QComboBox(self.ConfigBox)
        self.MoboManufacturercomboBox.addItem("")
        self.MoboManufacturercomboBox.addItem("")
        self.MoboManufacturercomboBox.addItem("")
        self.MoboManufacturercomboBox.setObjectName(u"MoboManufacturercomboBox")
        self.MoboManufacturercomboBox.setGeometry(QRect(308, 30, 111, 22))
        font2 = QFont()
        font2.setBold(False)
        self.MoboManufacturercomboBox.setFont(font2)
        self.MoboManufactureLabel = QLabel(self.ConfigBox)
        self.MoboManufactureLabel.setObjectName(u"MoboManufactureLabel")
        self.MoboManufactureLabel.setGeometry(QRect(10, 30, 341, 16))
        self.MoboManufactureLabel.setFont(font2)
        self.BlacklistIDsLabel = QLabel(self.ConfigBox)
        self.BlacklistIDsLabel.setObjectName(u"BlacklistIDsLabel")
        self.BlacklistIDsLabel.setGeometry(QRect(10, 70, 341, 16))
        self.BlacklistIDsLabel.setFont(font2)
        self.BlacklistIDsCheckbox = QCheckBox(self.ConfigBox)
        self.BlacklistIDsCheckbox.setObjectName(u"BlacklistIDsCheckbox")
        self.BlacklistIDsCheckbox.setGeometry(QRect(400, 70, 20, 20))
        self.LogBox = QGroupBox(self.centralwidget)
        self.LogBox.setObjectName(u"LogBox")
        self.LogBox.setGeometry(QRect(10, 230, 431, 281))
        self.LogBox.setFont(font1)
        self.Log = QTextEdit(self.LogBox)
        self.Log.setObjectName(u"Log")
        self.Log.setGeometry(QRect(10, 20, 411, 251))
        self.Log.setStyleSheet(u"")
        self.Log.setReadOnly(True)
        self.Log.setTextInteractionFlags(Qt.NoTextInteraction)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 21))
        self.menuMade_by_the_fern = QMenu(self.menubar)
        self.menuMade_by_the_fern.setObjectName(u"menuMade_by_the_fern")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.MoboManufacturercomboBox, self.BlacklistIDsCheckbox)
        QWidget.setTabOrder(self.BlacklistIDsCheckbox, self.GoButton)

        self.menubar.addAction(self.menuMade_by_the_fern.menuAction())
        self.menuMade_by_the_fern.addAction(self.actionCheck_out_my_website)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Goodbye Nahimic", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionCheck_out_my_website.setText(QCoreApplication.translate("MainWindow", u"Check out my website!", None))
        self.GoButton.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.ConfigBox.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.MoboManufacturercomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"--Choose One--", None))
        self.MoboManufacturercomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Asus", None))
        self.MoboManufacturercomboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"MSI", None))

        self.MoboManufactureLabel.setText(QCoreApplication.translate("MainWindow", u"Motherboard manufacturer", None))
        self.BlacklistIDsLabel.setText(QCoreApplication.translate("MainWindow", u"Blacklist driver IDs (may help prevent it being reinstalled)", None))
        self.BlacklistIDsCheckbox.setText("")
        self.LogBox.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.Log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">[LOG] test :)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>", None))
        self.menuMade_by_the_fern.setTitle(QCoreApplication.translate("MainWindow", u"Made by the fern :)", None))
    # retranslateUi

