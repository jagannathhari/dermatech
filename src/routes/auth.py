from flask import Blueprint
from fla

auth_bp = Blueprint("auth",__name__)
@auth_bp.route('/login')
def login():
    # Handle login logic
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    # Handle logout logic
    return 'Logged out'
