from PyQt5 import QtCore, QtGui, QtWidgets
import source
from Pemasukan import Ui_Pemasukan
from Pengeluaran import Ui_Pengeluaran
from Riwayat import Ui_Riwayat


class Ui_MainWindow(QtWidgets.QMainWindow):
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

    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setObjectName("MainWindow")
        self.resize(400, 560)
        self.setMinimumSize(QtCore.QSize(400, 560))
        self.setMaximumSize(QtCore.QSize(400, 560))
        self.setMouseTracking(True)
        self.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 281, 141))
        self.label.setStyleSheet("image: url(:/newPrefix/logo mm.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnPemasukan = QtWidgets.QPushButton(self.centralwidget)
        self.btnPemasukan.clicked.connect(self.pemasukan)
        self.btnPemasukan.setGeometry(QtCore.QRect(70, 310, 261, 41))
        self.btnPemasukan.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPemasukan.setMouseTracking(False)
        self.btnPemasukan.setStyleSheet("border-radius: 5px;\n"
                                        "font: 57 10pt \"Montserrat Medium\";\n"
                                        "background-color: rgb(57, 171, 121);\n"
                                        "color: rgb(255, 255, 255);")
        self.btnPemasukan.setObjectName("btnPemasukan")
        self.btnPengeluaran = QtWidgets.QPushButton(self.centralwidget)
        self.btnPengeluaran.clicked.connect(self.pengeluaran)
        self.btnPengeluaran.setGeometry(QtCore.QRect(70, 360, 261, 41))
        self.btnPengeluaran.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPemasukan.setText(_translate("MainWindow", "Tambah Pemasukan"))
        self.btnPengeluaran.setText(_translate(
            "MainWindow", "Tambah Pengeluaran"))
        self.btnRiwayat.setText(_translate("MainWindow", "Riwayat"))
        self.label_3.setText(_translate("MainWindow", "Saldo Anda"))
        self.label_2.setText(_translate("MainWindow", "Money Manager © 2020 "))
        self.label_4.setText(_translate("MainWindow", "By: @harismuhajir"))
