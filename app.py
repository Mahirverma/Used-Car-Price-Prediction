from myproject import app
from flask import render_template, redirect, request, url_for, flash, abort,jsonify
import numpy as np
import pandas as pd
import seaborn as sns
import category_encoders as ce
# from flask_login import login_user, login_required, logout_user
# from myproject.models import User
# from myproject.forms import LoginForm, RegistrationForm
# from werkzeug.security import generate_password_hash, check_password_hash

import pickle
# from flask_login import login_user, login_required, logout_user
# from myproject.models import User
# from myproject.forms import LoginForm, RegistrationForm
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_migrate import Migrate
# from flaskext.mysql import MySQL

model=pickle.load(open('./randomforestregressor.pkl','rb'))
transformer=pickle.load(open('./Power_Transformer.pickle','rb'))
transformer2=pickle.load(open('./binaryencoder.pickle','rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    Name=request.form.get('name')
    Location=request.form.get('location')
    Fuel_Type=request.form.get('fuel_type')
    Transmission=request.form.get('transmission')
    Brand=request.form.get('brand')
    Owner_Type=request.form.get('owner_type')
    Year=request.form.get('year')
    Kilometers_Driven=request.form.get('kilometers_driven')
    Mileage=request.form.get('mileage')
    Engine=request.form.get('engine')
    Power=request.form.get('power')
    Seats=request.form.get('seats')
    
    
    data=pd.DataFrame({'Name':Name,
                       'Location':Location,
                       'Fuel_Type':Fuel_Type,
                       'Transmission':Transmission,
                       'Brand':Brand,
                       'Owner_Type':Owner_Type,
                       'Year':Year,
                       'Kilometers_Driven':Kilometers_Driven,
                       'Mileage':Mileage,
                       'Power':Power,
                       'Engine':Engine,
                       'Seats':Seats }, index=[0])
    print("\n\nForm data\t",data)
    transformation1 = {
    "First":3,
    "Second":2,
    "Third":1,
    "Fourth & Above":0
    }
    data['Owner_Type']=data['Owner_Type'].map(transformation1)
    
    print("\n\ndata\t",data)
    
    nominal_data=['Name','Location','Fuel_Type','Transmission','Brand']
    binaryencoder=transformer2(cols=nominal_data)
    data=binaryencoder.transform(data)
    print("\n\ndata", data)
    
    new_data=pd.DataFrame(transformer.transform(data),columns=data.columns,index=data.index)
    print("\n\nnew data",new_data)
    
    
    prediction=model.predict(data)
    print("\n\n\n\nPrediction:\t",prediction)
    
#     if ((Owner_Type == 'First') or (Owner_Type == 'first')):
#         Owner_Type=3
#     elif ((Owner_Type == 'Second') or (Owner_Type == 'second')):
#         Owner_Type=2
#     elif ((Owner_Type == 'Third') or (Owner_Type == 'third')):
#         Owner_Type=1
#     else:
#         Owner_Type=0
            
#     nominal_data=[Name,Location,Fuel_Type,Transmission,Brand]
#     print("\n\nFeatures:\t",nominal_data)
#     Name=str(''.join(ce.BinaryEncoder(Name)))
#     Location=str(''.join(ce.BinaryEncoder(Location)))
#     Fuel_Type=str(''.join(ce.BinaryEncoder(Fuel_Type)))
#     Transmission=str(''.join(ce.BinaryEncoder(Transmission)))
#     Brand=str(''.join(ce.BinaryEncoder(Brand)))
    
#     print("\n\nFeatures:\t",nominal_data)
    
#     features=[Name,Location,Fuel_Type,Transmission,Brand,Owner_Type,Year,Kilometers_Driven,Mileage,Power,Engine,Seats]
#     final_features=transformer.fit_transform(features)
    
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You logged out!')
#     return redirect(url_for('home'))

# @app.route('/login',methods=['GET',['POST']])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user=User.query.filter(email=form.email.data).first()
#         if user.check_password(form.password.data) and user is not None:
#             login_user(user)
#             flash('You logged in successfully')

#             next=request.args.get('next')
#             if next == None or not next[0]=='/':
#                 next=url_for('home')

#             return redirect(next)
#     return render_template('login.html',form=form)

# @app.route('/register',methods=['GET',['POST']])
# def register():
#     form = RegistrationForm()

#     if form.validate_on_submit():
#         user = User(email=form.email.data,
#                     username=form.username.data,
#                     password=form.password.data)

#         db.session.add(user)
#         db.session.commit()
#         flash('Thanks for registering! You can login now!')
#         return redirect(url_for('login'))
#     return render_template('register.html',form=form)



if __name__ == '__main__':
    app.run(debug=True) 
