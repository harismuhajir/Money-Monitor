import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from Login.Login import Ui_Login as Login
from Register.Register import Ui_Register as Register
from dotenv import load_dotenv
from pathlib import Path
import os
import pymysql


class WindowSelector:
    def __init__(self):
        self.login_view = Login()
        self.login_view.switchWindow.connect(self.switch_window)
        self.register_view = Register()
        self.show_window("LOGIN")

    def show_window(self, window):
        if window == "LOGIN":
            self.current_window = self.login_view
            self.current_window.show()
        elif window == "REGISTER":
            self.current_window = self.register_view
            self.current_window.show()

    def switch_window(self, window):
        self.current_window.close()
        self.show_window(window)


def setupDb():
    host = os.getenv("DB_HOST")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_DATABASE")

    try:
        db = pymysql.connect(host, username, password, database)
    except pymysql.MySQLError as e:
        print(e)
        return False

    return db


if __name__ == '__main__':
    app = QApplication(sys.argv)
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    db = setupDb()

    if not db == False:
        window_selector = WindowSelector()
        aex = app.exec_()
        db.close()
        sys.exit(aex)
