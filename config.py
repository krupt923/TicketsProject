import os

db_host = os.environ.get('DB_HOST', default='3.21.158.108') # <-- Put your DB IP here
db_name = os.environ.get('DB_NAME', default='dashboard')
db_password = os.environ.get('DB_PASSWORD', default='secure_password')
db_port = os.environ.get('DB_PORT', default='5432')
db_user = os.environ.get('DB_USERNAME', default='dashboard')

SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"