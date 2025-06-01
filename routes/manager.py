from flask import Blueprint, render_template, request, flash, session, url_for
from extensions import login_manager, db, current_year
from flask_login import current_user

manager = Blueprint('manager', __name__, static_folder='static', template_folder='templates')


@manager.route('/', methods=['GET', 'POST'])
def home():
    return render_template('manager.html', logged_in=current_user.is_authenticated,
                           current_year=current_year)