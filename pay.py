from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel
Form, Window = uic.loadUiType("pay.ui")
from main import main_Ui

class Pay_Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Pay_Ui, self).__init__()
        self.setupUi(self)
        self.btnHome.clicked.connect(self.btnHomePressed)

    def btnHomePressed(self):
        self.window = main_Ui()
        self.window.show()
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Pay_Ui()
    w.setWindowTitle('Внесение платежа по кредиту МФО «‎Купи не Копи»‎')
    w.show()  # show window
    sys.exit(app.exec_())