from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'
db = SQLAlchemy(app)

from APP import routes  # import routes
