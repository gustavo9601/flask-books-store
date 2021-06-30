from app.models.entities.User import User


class UserModel:

    @classmethod
    def login(self, db, user: User):
        try:
            connection = db.connect()
            cursor = connection.cursor()
            sql = """
            SELECT id, user, password FROM users WHERE user = %s
            """
            cursor.execute(sql, (user.user,))
            data = cursor.fetchone()
            print(data)
            if data:
                encrypt_password = user.encrypt_password(data[2])
                if user.check_password(encrypt_password, user.password):
                    user_logged = User(data[0], data[1], None, None)
                    return user_logged
                else:
                    return None
            else:
                return None

        except Exception as ex:
            raise Exception(ex)