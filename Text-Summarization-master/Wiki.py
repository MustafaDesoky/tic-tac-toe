# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wiki.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import bs4 as bs
import urllib.request
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq


class Ui_WikiWindow(object):
    # Getting the data
    def get_data(self, url_input):
        try:
            source = urllib.request.urlopen(url_input).read()
            '''
                         ' lxml' = ' html.parser' They are used for reading html code 
                         serves as the basis for parsing text files formatted in HTML
            '''

            soup = bs.BeautifulSoup(source, 'lxml')

            # Loop for finding p tags in html code which we're gonna sum up
            text = ""
            for paragraph in soup.findAll('p'):
                # the .text() method convert the paragraph from html to txt
                text += paragraph.text

            # Here we're getting the header tag H1 of the page, Then printing it in the plainText
            title = soup.find('h1')
            self.summary_plainTextEdit.appendPlainText(title.text + ":")
            self.summary_plainTextEdit.appendPlainText("------------------------------")

            # Calling the method summarize with  text and num of words you want per sentence and number of sentence
            self.summarize(text)

        except:
            self.statusbar.showMessage("Check your internet connection or the URL you've entered")
            # https://en.wikipedia.org/wiki/Artificial_intelligence

    # Pre-processing the text
    def summarize(self, text):
        # The 1st copy of the text to remove all but the ( '.', ',') to recognize the sentences
        text = re.sub(r"\[[0-9]*\]", " ", text)
        text = re.sub(r"\s+", " ", text)

        # The 2nd copy of the text to remove all to recognize the words
        # symbols LIKE '! @ # $ % ^ & * ( ) = / - + . | : ; " | \ } { ] [ , < > . ? \ ' '
        clean_text = text.lower()
        clean_text = re.sub(r"\W", " ", clean_text)
        clean_text = re.sub(r"\d", " ", clean_text)
        clean_text = re.sub(r"\s+", " ", clean_text)

        sentences = sent_tokenize(text)

        # Gettin' the stop words
        stop_words = set(stopwords.words("english"))

        # Dictionary for counting the word
        word2count = {}
        for word in word_tokenize(clean_text):
            if word not in stop_words:
                if word not in word2count.keys():
                    word2count[word] = 1
                else:
                    word2count[word] += 1

        for key in word2count.keys():
            word2count[key] = word2count[key] / max(word2count.values())

        sent2score = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word2count.keys():
                    if sentence not in sent2score.keys():
                        sent2score[sentence] = word2count[word]
                    else:
                        sent2score[sentence] += word2count[word]

        # Determine the number of sentence and the num of words per each
        try:
            best_sentences = heapq.nlargest(int(self.sentences_num.text()), sent2score, key=sent2score.get)
        except:
            best_sentences = heapq.nlargest(int(len(sent2score.keys()) / 2), sent2score, key=sent2score.get)

        # Show the sentences in the plainText
        for sentence in best_sentences:
            self.summary_plainTextEdit.appendPlainText(sentence + "\n")
        self.summary_plainTextEdit.setStatusTip(
            "Summarized " + str(int(len(sent2score.keys()))) + " sentences into " + str(
                int(len(best_sentences))) + " sentences")

    def setupUi(self, WikiWindow):
        WikiWindow.setObjectName("WikiWindow")
        WikiWindow.setWindowModality(QtCore.Qt.NonModal)
        WikiWindow.resize(594, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WikiWindow.sizePolicy().hasHeightForWidth())
        WikiWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/wikipedia-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WikiWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(WikiWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setMaximumSize(QtCore.QSize(80, 70))
        self.start_btn.setObjectName("start_btn")

        self.start_btn.setStatusTip("Start...")
        self.start_btn.clicked.connect(self.start)

        self.gridLayout.addWidget(self.start_btn, 1, 6, 1, 1)
        self.input_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_lineEdit.sizePolicy().hasHeightForWidth())
        self.input_lineEdit.setSizePolicy(sizePolicy)
        self.input_lineEdit.setMinimumSize(QtCore.QSize(450, 0))
        self.input_lineEdit.setMaximumSize(QtCore.QSize(1024, 70))

        self.input_lineEdit.setClearButtonEnabled(True)

        self.input_lineEdit.setObjectName("input_lineEdit")
        self.gridLayout.addWidget(self.input_lineEdit, 1, 0, 1, 6)
        self.summary_label = QtWidgets.QLabel(self.centralwidget)
        self.summary_label.setObjectName("summary_label")
        self.gridLayout.addWidget(self.summary_label, 4, 0, 1, 1)
        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setMaximumSize(QtCore.QSize(70, 70))
        self.url_label.setObjectName("url_label")
        self.gridLayout.addWidget(self.url_label, 0, 0, 1, 1)

        self.sentences_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sentences_label.sizePolicy().hasHeightForWidth())
        self.sentences_label.setSizePolicy(sizePolicy)
        self.sentences_label.setMinimumSize(QtCore.QSize(70, 0))
        self.sentences_label.setMaximumSize(QtCore.QSize(150, 70))
        self.sentences_label.setObjectName("sentences_label")
        self.gridLayout.addWidget(self.sentences_label, 2, 0, 1, 1)

        self.sentences_num = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sentences_num.sizePolicy().hasHeightForWidth())
        self.sentences_num.setSizePolicy(sizePolicy)
        self.sentences_num.setMaximumSize(QtCore.QSize(40, 70))
        self.sentences_num.setObjectName("sentences_num")
        self.gridLayout.addWidget(self.sentences_num, 2, 1, 1, 1)

        self.summary_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.summary_plainTextEdit.setObjectName("summary_plainTextEdit")
        self.gridLayout.addWidget(self.summary_plainTextEdit, 5, 0, 1, 7)
        WikiWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WikiWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        WikiWindow.setMenuBar(self.menubar)

        file_menu = self.menubar.addMenu("File")
        edit_menu = self.menubar.addMenu("Edit")

        save_file = QtWidgets.QAction("Save As...", WikiWindow)
        save_file.setShortcut("Ctrl+S")
        save_file.setStatusTip('Save file...')
        save_file.triggered.connect(self.saveFile)

        quit_action = QtWidgets.QAction("Exit", WikiWindow)
        quit_action.setShortcut("Esc")
        quit_action.setStatusTip('Quit WikiWindow')
        quit_action.triggered.connect(WikiWindow.close)

        file_menu.addAction(save_file)
        file_menu.addAction(quit_action)

        clear_action = QtWidgets.QAction("Clear all", WikiWindow)
        clear_action.setShortcut("Ctrl+D")  # delete whats in the plaintext
        clear_action.setStatusTip('Empty all fields ')
        clear_action.triggered.connect(lambda: self.summary_plainTextEdit.clear())
        clear_action.triggered.connect(lambda: self.input_lineEdit.clear())

        edit_menu.addAction(clear_action)

        self.statusbar = QtWidgets.QStatusBar(WikiWindow)
        self.statusbar.setObjectName("statusbar")
        WikiWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WikiWindow)
        QtCore.QMetaObject.connectSlotsByName(WikiWindow)

    def retranslateUi(self, WikiWindow):
        _translate = QtCore.QCoreApplication.translate
        WikiWindow.setWindowTitle(_translate("WikiWindow", "Summarize from Wiki"))
        self.sentences_label.setText(_translate("WikiWindow", "Number of Sentences :"))
        self.start_btn.setText(_translate("WikiWindow", "Summarize"))
        self.summary_label.setText(_translate("WikiWindow", "Summary :"))
        self.url_label.setText(_translate("WikiWindow", "Enter Url :"))

    def start(self):
        self.summary_plainTextEdit.clear()
        self.get_data(self.input_lineEdit.text())

    def saveFile(self):
        try:
            name = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File')[0]
            file = open(name, 'w')
            text = self.summary_plainTextEdit.toPlainText()
            file.write(text)
            file.close()
        except:
            self.statusbar.showMessage("Canceled")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    WikiWindow = QtWidgets.QMainWindow()
    ui = Ui_WikiWindow()
    ui.setupUi(WikiWindow)
    WikiWindow.show()
    sys.exit(app.exec_())
