# Form implementation generated from reading ui file 'D:\__MY_PROJECT__\Python\ControlAxle\ui\base_qt_ui\ui_graph.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Graph(object):
    def setupUi(self, Graph):
        Graph.setObjectName("Graph")
        Graph.resize(1130, 160)
        Graph.setMinimumSize(QtCore.QSize(1130, 160))
        Graph.setMaximumSize(QtCore.QSize(1130, 160))
        self.button_check = QtWidgets.QPushButton(parent=Graph)
        self.button_check.setGeometry(QtCore.QRect(525, 130, 70, 20))
        self.button_check.setObjectName("button_check")
        self.lineEdit = QtWidgets.QLineEdit(parent=Graph)
        self.lineEdit.setGeometry(QtCore.QRect(60, 100, 1000, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=Graph)
        self.label.setGeometry(QtCore.QRect(10, 105, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Graph)
        QtCore.QMetaObject.connectSlotsByName(Graph)

    def retranslateUi(self, Graph):
        _translate = QtCore.QCoreApplication.translate
        Graph.setWindowTitle(_translate("Graph", "Dialog"))
        self.button_check.setText(_translate("Graph", "Cheсk"))
        self.label.setText(_translate("Graph", "Code"))
