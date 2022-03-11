DEBUG = True

# 'mysql+mysqlconnector://root:xxxxx@localhost:3306/test?charset=utf8'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DB_URL = 'mysql+mysqlconnector://{}:{}@{}:{}/flask_learn?charset=utf8' \
    .format(USERNAME, PASSWORD, HOST, PORT)

SQLALCHEMY_DATABASE_URI =DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'RJQEJRKQJRKEQWFDS'
