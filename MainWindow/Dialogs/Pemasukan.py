from PyQt5 import QtCore, QtGui, QtWidgets
from Repositories.MoneyRepository import Money


class Ui_Pemasukan(QtWidgets.QDialog):
    setBalance = QtCore.pyqtSignal(int)

    def __init__(self, parent, db, userId):
        super(Ui_Pemasukan, self).__init__(parent)
        self.userId = userId
        self.db = db

        self.setObjectName("Dialog")
        self.resize(360, 300)
        self.setMinimumSize(QtCore.QSize(360, 300))
        self.setMaximumSize(QtCore.QSize(360, 300))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(57, 171, 121);")
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(130, 70, 191, 31))
        self.dateEdit.setDateTime(QtCore.QDateTime(
            QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(40, 71, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(40, 121, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(40, 171, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(40, 221, 281, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("border-radius: 5px;\n"
                                      "font: 57 10pt \"Montserrat Medium\";\n"
                                      "background-color: rgb(57, 171, 121);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.insertPemasukan)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(130, 170, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 191, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Tambah Pemasukan"))
        self.label_4.setText(_translate("Dialog", "Tanggal"))
        self.label_5.setText(_translate("Dialog", "Nominal"))
        self.label_6.setText(_translate("Dialog", "Keterangan"))
        self.pushButton.setText(_translate("Dialog", "Tambah"))
        self.lineEdit.setPlaceholderText(
            _translate("Dialog", "Masukkan sumber pemasukan"))
        self.lineEdit_2.setPlaceholderText(
            _translate("Dialog", "Masukkan nominal pemasukan"))

    def insertPemasukan(self):
        error = False
        errorMessage = ""

        if not self.lineEdit.text().strip():
            error = True
            errorMessage += "Nominal wajib diisi\n"
        if not self.lineEdit_2.text().strip():
            error = True
            errorMessage += "Keterangan wajib diisi\n"
        if (not error) and (not self.lineEdit_2.text().strip().isnumeric()):
            error = True
            errorMessage += "Nominal harus berisi angka\n"
        elif (not error) and (int(self.lineEdit_2.text().strip()) < 0):
            error = True
            errorMessage += "Nominal tidak boleh berisi angka negatif"

        if(error):
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Critical,
                "Error",
                errorMessage
            ).exec()
        else:
            dateS = self.dateEdit.text().split("/")
            (result, error) = Money(self.db).insertIncome(
                int(self.lineEdit_2.text().strip()),
                self.lineEdit.text(),
                str(2020 + int(dateS[2])) + "-" + dateS[1] + "-" + dateS[0],
                self.userId
            )
            if error:
                QtWidgets.QMessageBox(
                    QtWidgets.QMessageBox.Critical,
                    "Error",
                    "Database error"
                ).exec()
            else:
                self.setBalance.emit(result)
                self.close()
