from app.orator.user import User
from app.orator.permission import Permission

class DDDSampleRpository:

    @staticmethod
    def index():
        return User \
            .select(
                "users.id", "users.name", "users.email", "users.birth_date",
                "users.permission_id", "permissions.permission"
            ) \
            .join('permissions', 'users.permission_id', '=', 'permissions.id') \
            .get() \
            .serialize()

    @staticmethod
    def show(id):
        return User \
            .select(
                "users.id", "users.name", "users.email", "users.birth_date",
                "users.permission_id", "permissions.permission"
            ) \
            .join('permissions', 'users.permission_id', '=', 'permissions.id') \
            .find(id) \
            .serialize()