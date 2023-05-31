from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from Ui_MainWindow import Ui_MainWindow

from gpt import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.sendButton.clicked.connect(self.btnsendclick)
        self.ui.clearButton.clicked.connect(self.btnclearclick)
        self.ui.pushButton_2.clicked.connect(self.certenkeyfunc)
        self.chatgpt=GPT()

    def btnsendclick(self):
        inputtext = self.ui.sendtextEdit.toPlainText()
        if inputtext != "":
            
            outputtext = self.chatgpt.askgpt(inputtext)

            self.ui.textEdit.append('-------------------------------------------------')
            self.ui.textEdit.append(outputtext)
        

    def btnclearclick(self):
        self.ui.textEdit.clear()

    def certenkeyfunc(self):
        self.chatgpt.key = self.ui.textEdit_3.toPlainText()
        self.ui.keylabel.setText('设定密钥为：'+self.chatgpt.key)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()