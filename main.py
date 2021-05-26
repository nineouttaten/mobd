from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel
Form, Window = uic.loadUiType("main_window.ui")

class main_Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(main_Ui, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.btnGive.clicked.connect(self.btnGivePressed)
        self.btnPay.clicked.connect(self.btnPayPressed)

    def btnPayPressed(self):
        from pay import Pay_Ui
        self.window = Pay_Ui()
        self.window.show()
        self.close()

    def btnGivePressed(self):
        from give import Give_Ui
        self.window = Give_Ui()
        self.window.show()
        self.close()

    def initUI(self):
        self.setWindowTitle('МФО «‎Купи не Копи»‎')
        self.setWindowIcon(QIcon('icons8----100.png'))
        self.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = main_Ui()
   # w.show()  # show window
    sys.exit(app.exec_())