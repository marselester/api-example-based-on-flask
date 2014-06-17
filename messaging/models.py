# coding: utf-8
from flask.ext.login import UserMixin


class User(UserMixin):
    def __init__(self, pk, name, password, access_key, secret_key):
        self.pk = pk
        self.name = name
        self.password = password
        self.access_key = access_key
        self.secret_key = secret_key

    def get_id(self):
        return self.pk

user_list = [
    User(
        pk='123',
        name='marsel',
        password='123',
        access_key='666',
        secret_key='werxhqb98rpaxn39848xrunpaw3489ruxnpa98w4rxn'
    )
]
