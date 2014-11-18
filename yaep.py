import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form (QDialog) :
    def __init__(self, parent=None) :
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an Expression, then Press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        #self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateGui)
        self.lineedit.editingFinished.connect(self.updateGui)
        self.setWindowTitle("Calculate")
    def updateGui(self):
        text = self.lineedit.text()
        self.lineedit.clear()
        try :
            self.browser.append("%s = <b>%s<b>" % (text, eval(text)))
        except :
            self.browser.append("<font color=red>%s</font> is an invalid expression" % (text))
app = QApplication(sys.argv)
x = Form()
x.show()
app.exec_()