from PyQt5 import QtCore, QtGui, QtWidgets
from MyUi import MyLabel
from Repositories.UserRepository import User
import source


class Ui_Register(QtWidgets.QWidget):
    switchWindow = QtCore.pyqtSignal(str)
    setUser = QtCore.pyqtSignal(str)

    def __init__(self, db):
        super().__init__()
        self.db = db

        self.setObjectName("Form")
        self.resize(400, 560)
        self.setMinimumSize(QtCore.QSize(400, 560))
        self.setMaximumSize(QtCore.QSize(400, 560))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 10, 281, 141))
        self.label.setStyleSheet("image: url(:/newPrefix/logo mm.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(70, 160, 261, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(70, 260, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(70, 230, 261, 31))
        self.label_3.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(70, 290, 261, 31))
        self.label_5.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 320, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(70, 190, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(57, 171, 121);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(70, 440, 261, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("border-radius: 5px;\n"
                                      "font: 57 10pt \"Montserrat Medium\";\n"
                                      "background-color: rgb(57, 171, 121);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.validate_register)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(70, 530, 261, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(120, 490, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = MyLabel(self)
        self.label_8.setGeometry(QtCore.QRect(240, 490, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_8.setObjectName("label_8")
        self.label_8.clicked.connect(self.gotoLogin)

        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 380, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(70, 350, 261, 31))
        self.label_9.setStyleSheet("font: 63 10pt \"Montserrat SemiBold\";")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Daftar"))
        self.label_4.setText(_translate("Form", "By: @harismuhajir"))
        self.lineEdit.setPlaceholderText(
            _translate("Form", "Masukkan username"))
        self.label_3.setText(_translate("Form", "Username"))
        self.label_5.setText(_translate("Form", "Password"))
        self.lineEdit_2.setPlaceholderText(
            _translate("Form", "Masukkan password"))
        self.label_6.setText(_translate("Form", "Daftar Akun"))
        self.pushButton.setText(_translate("Form", "Daftar"))
        self.label_2.setText(_translate("Form", "Money Manager © 2020 "))
        self.label_7.setText(_translate("Form", "Sudah punya akun? "))
        self.label_8.setText(_translate("Form", "Masuk"))
        self.lineEdit_3.setPlaceholderText(
            _translate("Form", "Ulangi password"))
        self.label_9.setText(_translate("Form", "Ulangi Password"))

    def gotoLogin(self):
        self.switchWindow.emit("LOGIN")

    def validate_register(self):
        error = False
        errorMessage = ""
        if not self.lineEdit.text().strip():
            error = True
            errorMessage += "Username tidak boleh kosong\n"
        if not self.lineEdit_2.text():
            error = True
            errorMessage += "Password tidak boleh kosong\n"
        if not self.lineEdit_3.text():
            error = True
            errorMessage += "Konfirmasi password tidak boleh kosong\n"
        if (not error) and (self.lineEdit_2.text() != self.lineEdit_3.text()):
            error = True
            errorMessage += "Konfirmasi password tidak cocok\n"

        if(error):
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Critical,
                "Error",
                errorMessage
            ).exec()
        else:
            (result, error) = User(self.db).register(
                self.lineEdit.text(),
                self.lineEdit_2.text()
            )
            if error:
                errorMessage = ""
                if error == "USERNAME_USED":
                    errorMessage = "Username telah terpakai"
                else:
                    errorMessage = "Database error"
                QtWidgets.QMessageBox(
                    QtWidgets.QMessageBox.Critical,
                    "Error",
                    errorMessage
                ).exec()
            else:
                QtWidgets.QMessageBox(
                    QtWidgets.QMessageBox.Information,
                    "Success",
                    "Akun berhasil dibuat"
                )
                self.setUser.emit(result)
                self.switchWindow.emit("MAIN")
