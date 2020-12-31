import uuid
import pymysql


class Money:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def getBalance(self, userId):
        getBalanceSql = "SELECT * FROM `money_infos` WHERE `user_id`=%s"
        self.cursor.execute(getBalanceSql, (userId))
        if self.cursor.rowcount > 0:
            balance = self.cursor.fetchone()
            return (int(balance[4]), False)
        else:
            return (False, True)

    def insertIncome(self, amount, info, date, userId):
        sql = """INSERT INTO `histories` 
        (`id`, `user_id`, `type`, `amount`, `info`, `date`) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        getBalanceSql = "SELECT * FROM `money_infos` WHERE `user_id`=%s"
        self.cursor.execute(getBalanceSql, (userId))
        if self.cursor.rowcount > 0:
            self.balance = self.cursor.fetchone()
        else:
            return (False, True)
        try:
            self.cursor.execute(
                sql, (str(uuid.uuid1()), userId, 0, amount, info, date))
            # Update pemasukan
            self.newIncome = self.balance[2] + int(amount)
            self.newBalance = self.balance[4] + int(amount)
            self.cursor.execute(
                "UPDATE `money_infos` SET `income`=%s, `outcome`=%s, `balance`=%s WHERE `user_id`=%s",
                (int(self.newIncome), int(self.balance[3]),
                 int(self.newBalance), userId)
            )
            self.db.commit()
            return (self.newBalance, False)
        except pymysql.DatabaseError as e:
            print(e)
            self.db.rollback()
            return (False, True)
