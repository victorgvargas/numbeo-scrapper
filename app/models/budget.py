class Budget:
    def __init__(self, id, user_id, income, net_budget, currency, region, family_size, city):
        self.id = id
        self.user_id = user_id
        self.income = income
        self.net_budget = net_budget
        self.currency = currency
        self.region = region
        self.family_size = family_size
        self.city = city

    @staticmethod
    def create(user_id, income, net_budget, currency, region, family_size, city):
        from flask_mysqldb import MySQL
        mysql = MySQL()
        cur = mysql.connection.cursor()
        
        # Check if the budgets table exists, and create it if it doesn't
        cur.execute("""
            CREATE TABLE IF NOT EXISTS budgets (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                income DECIMAL(10, 2) NOT NULL,
                net_budget DECIMAL(10, 2) NOT NULL,
                currency VARCHAR(10) NOT NULL,
                region VARCHAR(100) NOT NULL,
                family_size VARCHAR(100) NOT NULL,
                city VARCHAR(100) NOT NULL
            )
        """)
        
        # Insert the new budget record
        cur.execute("INSERT INTO budgets (user_id, income, net_budget, currency, region, family_size, city) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                    (user_id, income, net_budget, currency, region, family_size, city))
        mysql.connection.commit()
        cur.close()
        return True

    @staticmethod
    def get(user_id):
        from flask_mysqldb import MySQL
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM budgets WHERE user_id = %s", (user_id,))
        budgets = cur.fetchall()
        cur.close()
        return budgets

    @staticmethod
    def get_all():
        from flask_mysqldb import MySQL
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM budgets")
        budgets = cur.fetchall()
        cur.close()
        return budgets

    @staticmethod
    def update(id, user_id, income, net_budget, currency, region, family_size, city):
        from flask_mysqldb import MySQL
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("UPDATE budgets SET income=%s, net_budget=%s, currency=%s, region=%s, family_size=%s, city=%s WHERE id=%s AND user_id=%s", 
                    (income, net_budget, currency, region, family_size, city, id, user_id))
        mysql.connection.commit()
        cur.close()
        return True

    @staticmethod
    def delete(id, user_id):
        from flask_mysqldb import MySQL
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM budgets WHERE id=%s AND user_id=%s", (id, user_id))
        mysql.connection.commit()
        cur.close()
        return True