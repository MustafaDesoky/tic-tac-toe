from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2
import numpy as np
import pytesseract
from PIL import Image
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq


class Ui_ImageWindow(object):
    def get_string(self, img_path):
        # Tesseract Path
        pytesseract.pytesseract.tesseract_cmd = "Tesseract/tesseract.exe"

        # Read image with opencv
        img = cv2.imread(img_path)

        # Rescale the image, if needed.
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

        # Convert to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply dilation and erosion to remove some noise
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        # Apply blur to smooth out the edges
        img = cv2.GaussianBlur(img, (5, 5), 0)

        # Write image after removed noise
        cv2.imwrite("removed_noise.jpg", img)

        #  Apply threshold to get image with only black and white
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Write the image after apply opencv to do some ...
        cv2.imwrite("thres.jpg", img)

        # Recognize text with tesseract for python
        result = pytesseract.image_to_string(Image.open("thres.jpg"), lang='eng')

        # Remove template file
        os.remove("removed_noise.jpg")
        os.remove("thres.jpg")

        self.summarize(result)

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

    def setupUi(self, ImageWindow):
        ImageWindow.setObjectName("ImageWindow")
        ImageWindow.setWindowModality(QtCore.Qt.NonModal)
        ImageWindow.resize(594, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImageWindow.sizePolicy().hasHeightForWidth())
        ImageWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ImageWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ImageWindow)
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
        ImageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        ImageWindow.setMenuBar(self.menubar)

        file_menu = self.menubar.addMenu("File")
        edit_menu = self.menubar.addMenu("Edit")

        open_file = QtWidgets.QAction("Open...", ImageWindow)
        open_file.setShortcut("Ctrl+O")
        open_file.setStatusTip('Open a document file...')
        open_file.triggered.connect(self.openFile)

        save_file = QtWidgets.QAction("Save As...", ImageWindow)
        save_file.setShortcut("Ctrl+S")
        save_file.setStatusTip('Save file...')
        save_file.triggered.connect(self.saveFile)

        quit_action = QtWidgets.QAction("Exit", ImageWindow)
        quit_action.setShortcut("Esc")
        quit_action.setStatusTip('Quit ImageWindow')
        quit_action.triggered.connect(ImageWindow.close)

        file_menu.addAction(open_file)
        file_menu.addAction(save_file)
        file_menu.addAction(quit_action)

        clear_action = QtWidgets.QAction("Clear all", ImageWindow)
        clear_action.setShortcut("Ctrl+D")
        clear_action.setStatusTip('Empty all fields ')
        clear_action.triggered.connect(lambda: self.summary_plainTextEdit.clear())
        clear_action.triggered.connect(lambda: self.input_lineEdit.clear())

        edit_menu.addAction(clear_action)

        self.statusbar = QtWidgets.QStatusBar(ImageWindow)
        self.statusbar.setObjectName("statusbar")
        ImageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImageWindow)
        QtCore.QMetaObject.connectSlotsByName(ImageWindow)

    def retranslateUi(self, ImageWindow):
        _translate = QtCore.QCoreApplication.translate
        ImageWindow.setWindowTitle(_translate("ImageWindow", "Summarize from Image"))
        self.sentences_label.setText(_translate("ImageWindow", "Number of Sentences :"))
        self.start_btn.setText(_translate("ImageWindow", "Summarize"))
        self.summary_label.setText(_translate("ImageWindow", "Summary :"))
        self.url_label.setText(_translate("ImageWindow", "Path :"))

    def start(self):
        self.summary_plainTextEdit.clear()
        self.get_string(self.input_lineEdit.text())

    def openFile(self):
        # to get the first element (TheFileName) of the tuble
        name = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File')[0]
        self.input_lineEdit.setText(name)

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
    ImageWindow = QtWidgets.QMainWindow()
    ui = Ui_ImageWindow()
    ui.setupUi(ImageWindow)
    ImageWindow.show()
    sys.exit(app.exec_())
