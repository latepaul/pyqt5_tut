from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton("&Submit")
        self.quitButton = QPushButton("&Quit")

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)
        buttonLayout1.addWidget(self.submitButton)
        buttonLayout1.addWidget(self.quitButton)

        self.submitButton.clicked.connect(self.submitContact)
        self.quitButton.clicked.connect(self.formQuit)
        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Hello Qt")
        picture = QPicture()

    def submitContact(self):
        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please enter a name and address.")
            return
        elif name == "Paul":
            application_window.show()
        else:
            QMessageBox.information(self, "Success!",
                                    "Hello %s!" % name)

    def formQuit(self):
        QMessageBox.information(self,"Quit","You Wanna Quit? OK!")
        sys.exit(0)



class HelloWindow( QWidget ) :

   def __init__(self, parent=None ) :

      QWidget.__init__( self, parent )

      self.setGeometry( 300, 300, 400, 250 )

      self.setWindowTitle( "THIS IS A SIMPLE PyQt APPLICATION" )


   def paintEvent( self, event ) :

      painter = QPainter()
      painter.begin( self )

      painter.drawText( 80, 100, "Hello. I am a PyQt Application." )

      painter.drawText( 80, 150, "The coordinates of this line are (80,150)." )

      painter.end()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    application_window = HelloWindow()

    screen = Form()
    screen.show()

    sys.exit(app.exec_())