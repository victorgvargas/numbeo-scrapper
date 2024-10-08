import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '3fb7c8bcff355ef89878c1ecba78b566a58071cec2899361b3ef77ab7cccb0f5d5f9786a9a0d0cec9445ba5e718c1be6e5717d5bea52be41f6aef6a26765ba92b35f9ea5591020d167cb57dfb4fd6eb2060e714c50685f5b2de2b9798dc1fd38b072cb0951ec8f86d49d4d26f6af4eff449c99ce80e936087f8a34e9c5724aba8055d3f55bd2a1e2d317a727ed6026793b12fb880dd61f5cd15ea557336d5b5de23fa0e66ef271b4ca0c9d64056a0a8344733cf7023fc13ddbc3358c8087df954ec5f04a4c202bb893d9857d2e192e3e52cb3446fd2189bc1922f1c12358d7a084af0cc58200ecbda0690cdfe70fdb1d81ffe9741122a664f3745c319c755ffa')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'colcalc')