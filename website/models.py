
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id):
        self.id = str(user_id)
