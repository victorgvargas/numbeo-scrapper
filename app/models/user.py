from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id):
        from app import mysql
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()

        if not user:
            return None

        return User(id=user[0], username=user[1], password=user[2], email=user[3])

    @staticmethod
    def get_by_email(email):
        from app import mysql
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if not user:
            return None

        return User(id=user[0], username=user[1], password=user[2], email=user[3])

    @staticmethod
    def create(username, email, password):
        from app import mysql
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        mysql.connection.commit()
        cur.close()

        return User.get_by_email(email)