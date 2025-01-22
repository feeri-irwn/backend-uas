from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request
from flask_cors import CORS

#init db connect
app = Flask(__name__)
CORS(app,resources={r"/api/*": {"origins": "*"}},supports_credentials=True)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://feri-sql:1234@localhost:3306/uas-sql'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://uassql_easiermad:07aaad51578161deed4761c090d8722c793abd71@u4vzz.h.filess.io:3307/uassql_easiermad'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1234'

db = SQLAlchemy(app)


@app.route('/')
def home():
    return "Hallo, Saya Feri Irawan | NIM 21.83.0619 | KELAS TK01"
app.app_context().push()