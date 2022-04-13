'''
Auth Graphql API Models
'''

import bcrypt
import jwt

from common.extensions import db


SECRET_KEY = 'my_secret_password' #noqa


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    access_token = db.Column(db.Text)
    created_at = db.Column(db.Date)

    def save(self):
        if self.id == None:
             db.session.add(self)
        return db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'access_token': self.access_token,
            'created_at': str(self.created_at.strftime('%d-%m-%Y'))
        }

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def set_password(self, password):
        pwhash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = pwhash.decode('utf-8')

    def generate_token(self):
        if self.access_token:
            return self.access_token
        data = {'id': self.id, 'username': self.username}
        access_token = jwt.encode(data, SECRET_KEY, 'HS256')
        self.access_token = access_token
        self.save()
        return access_token

    def check_token(self, access_token):
        data = wt.decode(access_token, SECRET_KEY, algorithms='HS256')
        return self.access_token == access_token and self.id == data['id']
