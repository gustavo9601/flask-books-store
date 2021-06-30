from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Class should inherited from Mixim for the session works well
# UserMixin

class User(UserMixin):
    def __init__(self, id, user, password, type_user_id):
        self.id = id
        self.user = user
        self.password = password
        self.type_user_id = type_user_id

    def encrypt_password(self, password) -> str:
        password_encrypted = generate_password_hash(password)
        return password_encrypted

    def check_password(self, password_encrypted, password) -> bool:
        return check_password_hash(password_encrypted, password)
