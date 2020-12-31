import uuid
import bcrypt
import pymysql


class User:
    def __init__(self, db):
        self.cursor = db.cursor()
        self.db = db

    def register(self, username, password):
        sql = "SELECT * FROM `users` WHERE `username`=%s"
        self.cursor.execute(sql, username)
        if self.cursor.rowcount == 0:
            salt = bcrypt.gensalt()
            hashedPassword = bcrypt.hashpw(password.encode("utf-8"), salt)
            id = str(uuid.uuid4())
            sql = """INSERT INTO `users` (`id`, `username`, `password`)
            VALUES (%s, %s, %s)"""
            try:
                self.cursor.execute(sql, (id,
                                          username, hashedPassword))

                sql = "INSERT INTO `money_infos` (`id`, `user_id`, `income`, `outcome`, `balance`) VALUES (%s, %s, %s, %s, %s)"
                infoId = str(uuid.uuid4())
                self.cursor.execute(sql, (infoId, id, 0, 0, 0))
                self.db.commit()

                return (id, False)
            except pymysql.DatabaseError as e:
                print(e)
                self.db.rollback()
                return (False, "DB_ERROR")
        else:
            return (False, "USERNAME_USED")
