from PyQt5 import QtCore, QtGui, QtWidgets
import source
from Pemasukan import Ui_Pemasukan
from Pengeluaran import Ui_Pengeluaran
from Riwayat import Ui_Riwayat

class Ui_MainWindow(object):
    def pemasukan(self):
        self.pemasukan = QtWidgets.QDialog()
        self.ui = Ui_Pemasukan()
        self.ui.setupUi(self.pemasukan)
        self.pemasukan.show()

    def pengeluaran(self):
        self.pengeluaran = QtWidgets.QDialog()
        self.ui = Ui_Pengeluaran()
        self.ui.setupUi(self.pengeluaran)
        self.pengeluaran.show()

    def riwayat(self):
        self.riwayat = QtWidgets.QDialog()
        self.ui = Ui_Riwayat()
        self.ui.setupUi(self.riwayat)
        self.riwayat.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 560)
        MainWindow.setMinimumSize(QtCore.QSize(400, 560))
        MainWindow.setMaximumSize(QtCore.QSize(400, 560))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 281, 141))
        self.label.setStyleSheet("image: url(:/newPrefix/logo mm.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnPemasukan = QtWidgets.QPushButton(self.centralwidget)
        self.btnPemasukan.clicked.connect(self.pemasukan)
        self.btnPemasukan.setGeometry(QtCore.QRect(70, 310, 261, 41))
        self.btnPemasukan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPemasukan.setMouseTracking(False)
        self.btnPemasukan.setStyleSheet("border-radius: 5px;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"background-color: rgb(57, 171, 121);\n"
"color: rgb(255, 255, 255);")
        self.btnPemasukan.setObjectName("btnPemasukan")
        self.btnPengeluaran = QtWidgets.QPushButton(self.centralwidget)
        self.btnPengeluaran.clicked.connect(self.pengeluaran)
        self.btnPengeluaran.setGeometry(QtCore.QRect(70, 360, 261, 41))
        self.btnPengeluaran.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPengeluaran.setStyleSheet("border-radius: 5px;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"background-color: rgb(57, 171, 121);\n"
"color: rgb(255, 255, 255);")
        self.btnPengeluaran.setObjectName("btnPengeluaran")
        self.btnRiwayat = QtWidgets.QPushButton(self.centralwidget)
        self.btnRiwayat.clicked.connect(self.riwayat)
        self.btnRiwayat.setGeometry(QtCore.QRect(70, 410, 261, 41))
        self.btnRiwayat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRiwayat.setStyleSheet("border-radius: 5px;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"background-color: rgb(57, 171, 121);\n"
"color: rgb(255, 255, 255);")
        self.btnRiwayat.setObjectName("btnRiwayat")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 237, 171, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 240, 81, 31))
        self.label_3.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 500, 261, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 180, 261, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPemasukan.setText(_translate("MainWindow", "Tambah Pemasukan"))
        self.btnPengeluaran.setText(_translate("MainWindow", "Tambah Pengeluaran"))
        self.btnRiwayat.setText(_translate("MainWindow", "Riwayat"))
        self.label_3.setText(_translate("MainWindow", "Saldo Anda"))
        self.label_2.setText(_translate("MainWindow", "Money Manager © 2020 "))
        self.label_4.setText(_translate("MainWindow", "By: @harismuhajir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
