from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.booking import Booking
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# defaut page-- main dashboard-- the dashbaord is usally the back page (login and registration)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loginregistration')
def userinput():
    return render_template('loginregistration.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_reg(request.form):
        return redirect ('/loginregistration')

    # conditonal restarts below. Must bcrypt the password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "address": request.form['address'],
        "city": request.form['city'],
        "state": request.form['state'],
        
        "email": request.form['email'],
        "password" : pw_hash
    }

    # we need to save the data that is inputted by user
    user_id = User.save(data)
    # saves user_id into the session. User_id gets created after user inputs their information 
    session['user_id'] = user_id
    return redirect ('/')

@app.route('/login',methods=['POST'])
def login():

# we need to validate hash password
    print("request.form",request.form)
    if not User.validate_log(request.form):
        return redirect ('/loginregistration')

    # we need to get the id of the user to identify their information 
    
    one_user= User.get_user_by_email(request.form)

    session['user_id'] = one_user.id
    return redirect ('/')
    
    # login should fetch email address but should not save into database. This is a log in feature, info should already be saved.


    
@app.route('/dashboardmain')
def dashboard():

    data =     {
        'id': session['user_id']
    }

    user = User.get_user_by_id(data)
    

    return render_template("/" )

# if user is not in the session, redirect to logout page
# return redirect ('/logout')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
