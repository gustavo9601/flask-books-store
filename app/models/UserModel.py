from app.models.entities.TypeUser import TypeUser
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
            if data:
                if user.check_password(data[2], user.password):
                    user_logged = User(data[0], data[1], None, None)
                    return user_logged
                else:
                    return None
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_by_id(self, db, id):
        try:
            connection = db.connect()
            cursor = connection.cursor()
            sql = """
            SELECT u.id, u.user, tu.id, tu.name 
            FROM users as u
            INNER JOIN type_user as tu ON u.type_user_id = tu.id 
            WHERE u.id = %s
            """
            cursor.execute(sql, (id, ))
            data = cursor.fetchone()

            type_user = TypeUser(data[2], data[3])
            user_logged = User(data[0], data[1], None, type_user)

            return user_logged

        except Exception as ex:
            raise Exception(ex)