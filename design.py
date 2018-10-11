# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(469, 391)
        Dialog.setStyleSheet("QDialog{ background-color: rgb(255, 255, 255); }\n"
"QPushButton{\n"
" background-color: #FFFFFF;\n"
"    border: 1px solid #CCCCCC;\n"
"    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.075) inset;\n"
"    transition: border 0.2s linear 0s, box-shadow 0.2s linear 0s;\n"
"        border-radius: 4px;\n"
"    color: #555555;\n"
"    display:block;\n"
"      \n"
"    font-size: 14px;\n"
"        text-align:center;\n"
"    height: 20px;\n"
"    line-height: 20px;\n"
"    margin-bottom: 10px;\n"
"    padding: 4px 6px;\n"
"    vertical-align: middle;\n"
"        text-decoration:none;\n"
"}\n"
"QPushButton:hover, QPushButton:focus {\n"
"   border-color: rgba(82, 168, 236, 0.8);\n"
"   box-shadow: 0 1px 1px rgba(0, 0, 0, 0.075) inset, 0 0 8px rgba(82, 168, 236, 0.6);\n"
"   outline: 0 none;\n"
"}\n"
"\n"
"\n"
"")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(90, 30, 281, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 140, 272, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(120, 120, 221, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

