from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# remember to install bcrypt & flask

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/login', methods= ['post'])    
def login():
    is_valid = User.is_valid(request.form)

    if not is_valid:
        return redirect('/')

    return redirect('/')

@app.route('/register',methods=['POST'])
def save():

    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    # forgot to do this. remember to add to db
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')