# Form implementation generated from reading ui file 'D:\__MY_PROJECT__\Python\ControlAxle\ui\base_qt_ui\ui_graph.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Graph(object):
    def setupUi(self, Graph):
        Graph.setObjectName("Graph")
        Graph.resize(1130, 230)
        Graph.setMinimumSize(QtCore.QSize(1130, 230))
        Graph.setMaximumSize(QtCore.QSize(1130, 230))
        self.button_check = QtWidgets.QPushButton(parent=Graph)
        self.button_check.setGeometry(QtCore.QRect(1070, 163, 50, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        self.button_check.setFont(font)
        self.button_check.setObjectName("button_check")
        self.label_code = QtWidgets.QLabel(parent=Graph)
        self.label_code.setGeometry(QtCore.QRect(10, 133, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label_code.setFont(font)
        self.label_code.setObjectName("label_code")
        self.label_system1 = QtWidgets.QLabel(parent=Graph)
        self.label_system1.setGeometry(QtCore.QRect(10, 50, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label_system1.setFont(font)
        self.label_system1.setObjectName("label_system1")
        self.label_system2 = QtWidgets.QLabel(parent=Graph)
        self.label_system2.setGeometry(QtCore.QRect(10, 95, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label_system2.setFont(font)
        self.label_system2.setObjectName("label_system2")
        self.label_config = QtWidgets.QLabel(parent=Graph)
        self.label_config.setGeometry(QtCore.QRect(10, 17, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label_config.setFont(font)
        self.label_config.setObjectName("label_config")
        self.spinBox = QtWidgets.QSpinBox(parent=Graph)
        self.spinBox.setGeometry(QtCore.QRect(165, 12, 70, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(20)
        self.spinBox.setMaximum(10000)
        self.spinBox.setSingleStep(20)
        self.spinBox.setProperty("value", 20)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.label_config_2 = QtWidgets.QLabel(parent=Graph)
        self.label_config_2.setGeometry(QtCore.QRect(100, 15, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        self.label_config_2.setFont(font)
        self.label_config_2.setObjectName("label_config_2")
        self.label_code_2 = QtWidgets.QLabel(parent=Graph)
        self.label_code_2.setGeometry(QtCore.QRect(60, 203, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label_code_2.setFont(font)
        self.label_code_2.setObjectName("label_code_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Graph)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 200, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Graph)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 200, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_code_3 = QtWidgets.QLabel(parent=Graph)
        self.label_code_3.setGeometry(QtCore.QRect(160, 203, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label_code_3.setFont(font)
        self.label_code_3.setObjectName("label_code_3")
        self.label_code_4 = QtWidgets.QLabel(parent=Graph)
        self.label_code_4.setGeometry(QtCore.QRect(310, 203, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label_code_4.setFont(font)
        self.label_code_4.setObjectName("label_code_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Graph)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 200, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit = QtWidgets.QTextEdit(parent=Graph)
        self.textEdit.setGeometry(QtCore.QRect(60, 130, 1000, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.button_trans = QtWidgets.QPushButton(parent=Graph)
        self.button_trans.setGeometry(QtCore.QRect(1070, 130, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.button_trans.setFont(font)
        self.button_trans.setObjectName("button_trans")
        self.button_reset_count = QtWidgets.QPushButton(parent=Graph)
        self.button_reset_count.setGeometry(QtCore.QRect(480, 200, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        self.button_reset_count.setFont(font)
        self.button_reset_count.setObjectName("button_reset_count")

        self.retranslateUi(Graph)
        QtCore.QMetaObject.connectSlotsByName(Graph)

    def retranslateUi(self, Graph):
        _translate = QtCore.QCoreApplication.translate
        Graph.setWindowTitle(_translate("Graph", "Dialog"))
        self.button_check.setText(_translate("Graph", "Cheсk"))
        self.label_code.setText(_translate("Graph", "Code"))
        self.label_system1.setText(_translate("Graph", "SYS1"))
        self.label_system2.setText(_translate("Graph", "SYS2"))
        self.label_config.setText(_translate("Graph", "Conf"))
        self.label_config_2.setText(_translate("Graph", "Time, µs"))
        self.label_code_2.setText(_translate("Graph", "Axle"))
        self.lineEdit_2.setText(_translate("Graph", "0"))
        self.lineEdit_3.setText(_translate("Graph", "0"))
        self.label_code_3.setText(_translate("Graph", "Count SYS1"))
        self.label_code_4.setText(_translate("Graph", "Count SYS2"))
        self.lineEdit_4.setText(_translate("Graph", "0"))
        self.textEdit.setHtml(_translate("Graph", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("Graph", "Example: SYS1(0:1000us;   1:2500us;  0:4000us);   SYS2(0:1300us;   1:2800us;  0:4000us)                                                                                                        Example: SYS1(0:d1000us; 1:d1500us; 0:d1500us); SYS2(0:d1300us; 1:d1500us; 0:d1200us)"))
        self.button_trans.setText(_translate("Graph", "Trans"))
        self.button_reset_count.setText(_translate("Graph", "Reset"))
