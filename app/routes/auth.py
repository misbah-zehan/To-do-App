from flask import Blueprint, request, render_template, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': 'admin',
    'password': 'password123'
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['username'] = username  # Store the username in the session
            flash('Login successful!', 'success')
            #return redirect(url_for('home'))  # Redirect to the home page after successful login
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    return render_template('login.html')  # Render the login template for GET requests or failed login attempts

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))  # Redirect to the login page after logout