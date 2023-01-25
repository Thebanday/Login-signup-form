from flask import Flask, render_template, request, redirect, session
import hashlib

app = Flask(__name__)
app.secret_key = "secretkey"

#list to store all user information
users = []

#signup form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        profile_picture = request.form['profile_picture']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        pincode = request.form['pincode']

        #check if passwords match
        if password != confirm_password:
            return "Passwords do not match. Please try again."
        else:
            #hash password
            password = hashlib.sha256(password.encode()).hexdigest()

            #store user information
            user = {'first_name': first_name, 'last_name': last_name, 'profile_picture': profile_picture, 'username': username, 'email': email, 'password': password, 'address': address, 'city': city, 'state': state, 'pincode': pincode}
            users.append(user)
            return "Signup successful. Please login."
    else:
        return render_template('signup.html')

#login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #get form data
        username = request.form['username']
        password = request.form['password']

        #hash password
        password = hashlib.sha256(password.encode()).hexdigest()

        #check if user information is correct
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                if user['first_name'].startswith('Dr.'):
                    return redirect('/doctor_dashboard')
                else:
                    return redirect('/patient_dashboard')
        return "Invalid username or password. Please try again."
    else:
        return render_template('login.html')

#patient dashboard
@app.route('/patient_dashboard')
def patient_dashboard():
    if 'username' in session:
        for user in users:
            if user['username'] == session['username']:
                return render_template('patient_dashboard.html', user=user)
    else:
        return redirect('/login')

#doctor dashboard
@app.route('/doctor_dashboard')
def doctor_dashboard():
    if 'username' in session:
        for user in users:
            if user['username'] == session['username']:
                return render_template('doctor_dashboard.html', user=user)
    else:
        return redirect('/login')
