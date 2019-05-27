# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Backoffice_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.getCSV)
    def getCSV(self, Form):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self,'Open file','C:/Users/admin/Desktop/Internship')
        if filePath != "":
            print("Address",filePath)
            self.df = pd.read_csv(str(filePath))
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(847, 592)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 20, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 510, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(440, 120, 71, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(400, 120, 51, 21))
        self.label_6.setObjectName("label_6")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(200, 120, 71, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(280, 120, 51, 21))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 120, 51, 21))
        self.label_4.setObjectName("label_4")
        self.comboBox_6 = QtWidgets.QComboBox(Form)
        self.comboBox_6.setGeometry(QtCore.QRect(580, 120, 51, 21))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(520, 120, 61, 21))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 120, 61, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_7 = QtWidgets.QComboBox(Form)
        self.comboBox_7.setGeometry(QtCore.QRect(710, 120, 81, 21))
        self.comboBox_7.setObjectName("comboBox_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(640, 120, 61, 21))
        self.label_8.setObjectName("label_8")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(330, 120, 61, 21))
        self.comboBox_4.setObjectName("comboBox_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Back Office Software"))
        self.pushButton.setText(_translate("Form", "Show Report"))
        self.pushButton_2.setText(_translate("Form", "Import CSV File"))
        self.label_6.setText(_translate("Form", "Symbol:"))
        self.label_5.setText(_translate("Form", "Client ID:"))
        self.label_3.setText(_translate("Form", "User ID:"))
        self.label_4.setText(_translate("Form", "Exchange:"))
        self.label_7.setText(_translate("Form", "Strike Price:"))
        self.label_8.setText(_translate("Form", "Expiry Date:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

