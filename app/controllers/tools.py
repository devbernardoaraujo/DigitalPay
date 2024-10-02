from functools import wraps
from flask import abort, render_template
from flask_login import current_user
from app import app

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return render_template('login')
            if role == 'admin' and not current_user.is_admin():
                abort(403)  # Acesso negado
            elif role == 'editor' and not (current_user.is_editor() or current_user.is_admin()):
                abort(403)  # Acesso negado
            elif role == 'viewer' and not (current_user.is_viewer() or current_user.is_editor() or current_user.is_admin()):
                abort(403)  # Acesso negado
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html', error=error)