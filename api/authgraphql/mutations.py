"""
Auth GraghQL API mutations
"""

from datetime import date

from common.extensions import db

from .common import mutation
from .models import User


@mutation.field('login')
def resolve_login(_, info, username, password):
    response = {'success': False, 'errors': ['Invalid username or password']}
    if username and password:
        try:
            user = User.query.filter_by(username=username).first()
            if user:
                if user.check_password(password):
                    token = user.generate_token()

                    response['success'] = True
                    response['errors'] = None
                    response['user'] = user.to_dict()
        except Exception as e:
            response['errors'] = [str(e)]
    return response

@mutation.field('createUser')
def create_post_resolver(obj, info, username, password):
    response = {'success': False, 'errors': ['Invalid username or password']}
    if username and password:
        try:
            user = User.query.filter_by(username=username).first()
            if user:
                response['errors'] = ['Username duplicated!']
            else:
                today = date.today()
                user = User(username=username, created_at=today)
                user.set_password(password)
                user.save()

                response['success'] = True
                response['errors'] = None
                response['user'] = user.to_dict()
        except Exception as e:
            response['errors'] = [str(e)]
    return response
