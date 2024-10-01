import os


SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')

connection_string = 'postgresql://postgres:1212335@localhost:5432/project'

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'connection_string')

