from flask import Blueprint, render_template, request, flash, session, url_for
from werkzeug.utils import redirect

from extensions import login_manager, db, current_year
from flask_login import current_user, login_required
from models.member import Member, Role, VidEditProject

manager = Blueprint('manager', __name__, static_folder='static', template_folder='templates/manager')


@manager.route('/', methods=['GET', 'POST'])
@login_required
def home():
    roles = current_user.role
    admin = db.session.query(Role).filter_by(name='admin').one_or_none()
    # --------------------------------------------------- FORM ACTION ----------------------------------------------- #
    # ------------------------------------------------ ASSIGN/REMOVE ROLE ------------------------------------------- #
    if request.method == 'POST':
        if request.form.get('submit') == 'assign-role':
            email = request.form.get('email')
            role_name = request.form.get('role')
            role = db.session.query(Role).filter_by(name=role_name).one_or_none()
            member = db.session.query(Member).filter_by(email=email).one_or_none()
            if role not in member.role:
                member.role.append(role)
                db.session.commit()
                print(member.role)
                flash('Role assigned successfully', 'success')
            else:
                flash('Role already assigned!', 'error')

        if request.form.get('submit') == 'remove-role':
            email = request.form.get('email')
            role_name = request.form.get('role')
            role = db.session.query(Role).filter_by(name=role_name).one_or_none()
            member = db.session.query(Member).filter_by(email=email).one_or_none()
            print(role)
            print(member)
            if role in member.role:
                member.role.remove(role)
                db.session.commit()
                flash('Role removed successfully', 'success')
                print(member.role)
                return redirect(request.url)
            else:
                flash('Not assigned any such role!', 'error')
                return redirect(request.url)

    # ---------------------------------------------- ASSIGN/REMOVE PROJECT ------------------------------------------ #
    if request.form.get('submit') == 'assign-project':
        member = request.form.get('promotion-team-member')
        project = request.form.get('promotion-project')
        role = request.form.get('project-role')

    # -------------------------------------------------- HTML VARIABLES --------------------------------------------- #
    if admin in current_user.role:
        roles = db.session.query(Role).all()
        promotion_team_members_list = []
        promotion_project_list = []
        project_roles_list = []


        return render_template('manager.html', logged_in=current_user.is_authenticated,
                               current_year=current_year, roles=roles)
    else:
        return render_template('admin_only_area.html', logged_in=current_user.is_authenticated)