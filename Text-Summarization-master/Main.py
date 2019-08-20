# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Wiki import Ui_WikiWindow
from Word import Ui_WordWindow
from Image import Ui_ImageWindow
from PDF import Ui_PdfWindow


class Ui_MainWindow(object):
    # Open Wiki Window
    def openWikiWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WikiWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWordWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WordWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openImageWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ImageWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPdfWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PdfWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 426)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/summarize-icon-9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.wiki_btn = QtWidgets.QPushButton(self.centralwidget)
        self.wiki_btn.setObjectName("wiki_btn")

        self.wiki_btn.clicked.connect(self.openWikiWindow)

        self.gridLayout.addWidget(self.wiki_btn, 7, 0, 1, 1)
        self.wiki_pic = QtWidgets.QLabel(self.centralwidget)
        self.wiki_pic.setEnabled(True)
        self.wiki_pic.setMaximumSize(QtCore.QSize(90, 90))
        self.wiki_pic.setText("")
        self.wiki_pic.setPixmap(QtGui.QPixmap("icons/wikipedia-logo.png"))
        self.wiki_pic.setScaledContents(True)
        self.wiki_pic.setObjectName("wiki_pic")
        self.gridLayout.addWidget(self.wiki_pic, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 8, 1, 1, 1)
        self.doc_pic = QtWidgets.QLabel(self.centralwidget)
        self.doc_pic.setMaximumSize(QtCore.QSize(90, 90))
        self.doc_pic.setText("")
        self.doc_pic.setPixmap(QtGui.QPixmap("icons/doc.png"))
        self.doc_pic.setScaledContents(True)
        self.doc_pic.setObjectName("doc_pic")
        self.gridLayout.addWidget(self.doc_pic, 9, 2, 1, 1)
        self.doc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.doc_btn.setObjectName("doc_btn")

        self.doc_btn.clicked.connect(self.openWordWindow)

        self.gridLayout.addWidget(self.doc_btn, 13, 2, 1, 1)
        self.pdf_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pdf_btn.setObjectName("pdf_btn")

        self.pdf_btn.clicked.connect(self.openPdfWindow)

        self.gridLayout.addWidget(self.pdf_btn, 13, 0, 1, 1)
        self.pdf_pic = QtWidgets.QLabel(self.centralwidget)
        self.pdf_pic.setMaximumSize(QtCore.QSize(90, 90))
        self.pdf_pic.setText("")
        self.pdf_pic.setPixmap(QtGui.QPixmap("icons/pdf.png"))
        self.pdf_pic.setScaledContents(True)
        self.pdf_pic.setObjectName("pdf_pic")
        self.gridLayout.addWidget(self.pdf_pic, 9, 0, 1, 1)
        self.image_btn = QtWidgets.QPushButton(self.centralwidget)
        self.image_btn.setObjectName("image_btn")

        self.image_btn.clicked.connect(self.openImageWindow)

        self.gridLayout.addWidget(self.image_btn, 7, 2, 1, 1)
        self.image_pic = QtWidgets.QLabel(self.centralwidget)
        self.image_pic.setMaximumSize(QtCore.QSize(90, 90))
        self.image_pic.setText("")
        self.image_pic.setPixmap(QtGui.QPixmap("icons/picture.png"))
        self.image_pic.setScaledContents(True)
        self.image_pic.setWordWrap(False)
        self.image_pic.setObjectName("image_pic")
        self.gridLayout.addWidget(self.image_pic, 6, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Summarization"))
        self.wiki_btn.setText(_translate("MainWindow", "Summarize from Wikipedia"))
        self.doc_btn.setText(_translate("MainWindow", "Summarize from Docment"))
        self.pdf_btn.setText(_translate("MainWindow", "Summarize from PDF"))
        self.image_btn.setText(_translate("MainWindow", "Summarize from Image"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
