import pickle
from flask import Flask,jsonify



app=Flask(__name__,static_folder='static')
# model=pickle.load(open('./randomforestregressor.pkl','rb'))
# transformer=pickle.load(open('./power.pickle','rb'))

# app.config['SECRET_KEY'] = 'mysecretkey'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_DB'] = 'db'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# db=MySQL(app)

# login_manager.init_app(app)
# login_manager.login_view='login'           