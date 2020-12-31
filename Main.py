import sys
from PyQt5.QtWidgets import QApplication
from Login.Login import Ui_Login as Login
from Register.Register import Ui_Register as Register


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_selector = WindowSelector()
    sys.exit(app.exec_())
