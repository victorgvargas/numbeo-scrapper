from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id):
        from flask_mysqldb import MySQL
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()

        if not user:
            return None

        return User(id=user['id'], username=user['username'], password=user['password'], email=user['email'])

    @staticmethod
    def get_by_email(email):
        from flask_mysqldb import MySQL
        mysql = MySQL()
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, password, email FROM users WHERE email = %s", (email,))
        user = cur.fetchone()  # Pode retornar None se não encontrar nada
        cur.close()

        print(f"User: {user}")
        
        if not user:
            return None  # Retorna None se nenhum usuário foi encontrado
        
        return User(id=user['id'], username=user['username'], password=user['password'], email=user['email'])

    @staticmethod
    def create(username, email, password):
        from flask_mysqldb import MySQL
        mysql = MySQL()
        cur = mysql.connection.cursor()

        # Verifica se o usuário já existe
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        existing_user = cur.fetchone()

        if existing_user:
            return None  # Ou lançar uma exceção personalizada

        # Inserir novo usuário
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        mysql.connection.commit()
        cur.close()

        return User.get_by_email(email)
    
    def get_session_token(self):
        from flask import current_app
        from itsdangerous import URLSafeTimedSerializer

        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps(self.id, salt=current_app.config['SECURITY_PASSWORD_SALT'])
    