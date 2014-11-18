# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printHam_widget.ui'
#
# Created: Tue Nov 18 19:18:56 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

import sys

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.printHam_btn = QtWidgets.QPushButton(Form)
        self.printHam_btn.setObjectName("printHam_btn")
        self.verticalLayout.addWidget(self.printHam_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Super Ham"))
        self.printHam_btn.setText(_translate("Form", "Print Ham"))
        self.printHam_btn.clicked.connect(self.printHam)

    def printHam(self):
        print("Ham!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())

