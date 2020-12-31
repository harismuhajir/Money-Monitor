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


def migrateDb(cursor):
    # Migrate user table
    sql = """CREATE TABLE IF NOT EXISTS users (id VARCHAR(100) NOT NULL, 
    username VARCHAR(255) NOT NULL, 
    password VARCHAR(100) NOT NULL, 
    PRIMARY KEY (id));
    """
    cursor.execute(sql)

    # Migrate history table
    sql = """CREATE TABLE IF NOT EXISTS `histories` ( 
        `id` VARCHAR(100) NOT NULL , 
        `user_id` VARCHAR(100) NOT NULL,
        `type` TINYINT NOT NULL , 
        `amount` BIGINT NOT NULL , 
        `info` TEXT NOT NULL , 
        `date` DATE NOT NULL , 
        PRIMARY KEY (`id`));
    """
    cursor.execute(sql)
    # Add relation history to user table
    sql = """ALTER TABLE `histories` 
    ADD CONSTRAINT `history_users_user_id_foreign` 
    FOREIGN KEY (`user_id`) 
    REFERENCES `users`(`id`) 
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor.execute(sql)

    # Migrate history table
    sql = """CREATE TABLE IF NOT EXISTS `money_infos` ( 
        `id` VARCHAR(100) NOT NULL , 
        `user_id` VARCHAR(100) NOT NULL UNIQUE,
        `income` BIGINT NOT NULL , 
        `outcome` BIGINT NOT NULL , 
        `balance` BIGINT NOT NULL ,
        PRIMARY KEY (`id`));
    """
    cursor.execute(sql)
    # Add relation history to user table
    sql = """ALTER TABLE `money_infos` 
    ADD CONSTRAINT `money_info_users_user_id_foreign` 
    FOREIGN KEY (`user_id`) 
    REFERENCES `users`(`id`) 
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor.execute(sql)

    # Add MIGRATED table for migrated status
    sql = """CREATE TABLE IF NOT EXISTS `migrated` (id INT(11) NOT NULL, PRIMARY KEY (id))"""
    cursor.execute(sql)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    db = setupDb()

    if not db == False:
        cursor = db.cursor()

        cursor.execute("SHOW TABLES LIKE 'migrated'")
        migrated = cursor.rowcount
        if(migrated == 0):
            migrateDb(cursor)

        window_selector = WindowSelector()
        aex = app.exec_()
        db.close()
        sys.exit(aex)
