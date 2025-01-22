from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#init db connect
app = Flask(__name__)
CORS(app,resources={r"/api/*": {"origins": "*"}},supports_credentials=True)
#CORS(app, origins=["http://localhost:5173"])

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://feri-sql:1234@localhost:3306/uas-sql'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://uassql_easiermad:07aaad51578161deed4761c090d8722c793abd71@u4vzz.h.filess.io:3307/uassql_easiermad'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1234'

# Use create_engine to enable connection pooling
engine = create_engine(
    app.config['SQLALCHEMY_DATABASE_URI'],
    pool_size=5,  # Jumlah koneksi dalam pool
    max_overflow=10,  # Jumlah koneksi yang bisa lebih dari pool_size
    pool_timeout=30,  # Waktu tunggu dalam detik untuk koneksi
    pool_recycle=1800  # Waktu hidup maksimum koneksi dalam detik (30 menit)
)

db = SQLAlchemy(app)
Session = sessionmaker(bind=engine)

@app.route('/')
def home():
    return "|21.83.0619 | Feri Irawan | backend-toko |"
app.app_context().push()