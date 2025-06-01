from flask import Blueprint, render_template, request, flash, session, url_for
from extensions import login_manager, db, current_year
from flask_login import current_user

from models.member import Member

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/', methods=['GET', 'POST'])
def home():

    return render_template('index.html', logged_in=current_user.is_authenticated,
                           current_year=current_year)


@main.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html', logged_in=current_user.is_authenticated,
                           current_year=current_year)


@main.route('/ad_samples', methods=['GET', 'POST'])
def ad_samples():
    return render_template('ad_samples.html', logged_in=current_user.is_authenticated,
                           current_year=current_year)

@main.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html', current_year=current_year)


@main.route('/terms_and_conditions')
def terms_and_conditions():
    return render_template('terms_and_conditions.html', current_year=current_year)
